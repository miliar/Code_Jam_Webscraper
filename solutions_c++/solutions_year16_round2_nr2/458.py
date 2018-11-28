#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
typedef long long ULL;

ULL pw[20];
typedef pair<LL, int> pr;
pr dp[2][20][3];
int vis[20][3];
int ID;
#define EQ 0
#define GR 1
#define LW 2

int CMP(int old, int a, int b) {
  if (old != EQ)
    return old;
  if (a > b)
    return GR;
  else if (a == b)
    return EQ;
  else
    return LW;
}

pr solve(int ind, int cmp, string &s1, string &s2, int p) {

  if (ind == s1.size())
    return pr(0, 1);

  pr &ret = dp[p][ind][cmp];
  int &tv = vis[ind][cmp];
  if (tv == ID)
    return ret;

  tv = ID;
  ret = pr(LLONG_MAX, 0);
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      int a, b;
      if (s1[ind] != '?')
        a = s1[ind] - '0';
      else
        a = i;
      if (s2[ind] != '?')
        b = s2[ind] - '0';
      else
        b = j;
      if (CMP(cmp, a, b) != LW) {
        LL k = (a - b);
        k *= pw[ind];
        pr n = solve(ind + 1, CMP(cmp, a, b), s1, s2, p);
        if (n.second) {
          ret.first = min(ret.first, k + n.first);
          ret.second = 1;
        }
      }
    }
  }
  return ret;
}
string r1, r2;
void Back(int ind, int cmp, string &s1, string &s2, int p) {
  if (ind == s1.size())
    return;
  pr &ret = dp[p][ind][cmp];
  if (!p) {
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        int a, b;
        if (s1[ind] != '?')
          a = s1[ind] - '0';
        else
          a = i;
        if (s2[ind] != '?')
          b = s2[ind] - '0';
        else
          b = j;
        if (CMP(cmp, a, b) != LW) {
          ULL k = (a - b);
          k *= pw[ind];
          pr n = solve(ind + 1, CMP(cmp, a, b), s1, s2, p);
          if (ret.first == k + n.first && n.second) {
            r1[ind] = a + '0';
            r2[ind] = b + '0';
            Back(ind + 1, CMP(cmp, a, b), s1, s2, p);
            return;
          }
        }
      }
    }
  } else {
    for (int j = 0; j < 10; j++) {
      for (int i = 0; i < 10; i++) {
        int a, b;
        if (s1[ind] != '?')
          a = s1[ind] - '0';
        else
          a = i;
        if (s2[ind] != '?')
          b = s2[ind] - '0';
        else
          b = j;
        if (CMP(cmp, a, b) != LW) {
          ULL k = (a - b);
          k *= pw[ind];
          pr n = solve(ind + 1, CMP(cmp, a, b), s1, s2, p);
          if (ret.first == k + n.first && n.second) {
            r1[ind] = a + '0';
            r2[ind] = b + '0';
            Back(ind + 1, CMP(cmp, a, b), s1, s2, p);
            return;
          }
        }
      }
    }
  }
}

string ss1,ss2;
int ret;
void update(string s1,string s2) {
  int k1 =0,k2=0;
  for(int i=0;i<s1.size();i++) {
    k1*=10;
    k1 += s1[i]-'0';
  }
  for(int i=0;i<s2.size();i++) {
      k2*=10;
      k2 += s2[i]-'0';
    }
  if(abs(k1-k2) < ret) {
    ret = abs(k1-k2);
  }
}
void BB(int ind,string &s1,string &s2, string &r1,string &r2) {
  if(ind == s1.size()) {

  }
}
int main() {
#ifndef ONLINE_JUDGE
  freopen("2.in", "r", stdin);
  freopen("2.out", "w", stdout);
#endif // ONLINE_JUDGE  ios::sync_with_stdio(false);  cin.tie(NULL);
  cout.tie(NULL);

  int T;
  cin >> T;
  for (int ic = 1; ic <= T; ic++) {
    string s1, s2;
    cin >> s1 >> s2;
    int t = s1.size();
    pw[t - 1] = 1;
    for (int i = t - 2; i >= 0; i--)
      pw[i] = pw[i + 1] * 10ll;

    ID++;
    pr n1 = solve(0, 0, s1, s2, 0);
    ID++;
    pr n2 = solve(0, 0, s2, s1, 1);

    if (n1.second && n2.second) {
      r1 = r2 = s1;
      if (n1.first < n2.first) {
        Back(0, 0, s1, s2, 0);
      } else if(n1.first > n2.first){
        Back(0, 0, s2, s1, 1);
        swap(r1, r2);
      } else {
        Back(0, 0, s1, s2, 0);
        typedef pair<string, string> pss;
        pss p1 = pss(r1,r2);
        Back(0, 0, s2, s1, 1);
        swap(r1, r2);
        pss p2 = pss(r1,r2);
        if(p1<=p2) {
          r1 =p1.first;
          r2 = p1.second;
        } else {
          r1 =p2.first;
          r2 = p2.second;
        }
      }
    } else if (n1.second) {
      r1 = r2 = s1;
      Back(0, 0, s1, s2, 0);
    } else if (n2.second) {
      r1 = r2 = s1;
      Back(0, 0, s2, s1, 1);
      swap(r1, r2);
    }
    //cout << s1 << " " << s2 << endl;
    cout << "Case #" << ic << ": ";
    cout << r1 << " " << r2 << endl;
  }
  return 0;

}
