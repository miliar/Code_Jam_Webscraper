#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

#define FOR(i,a,b) for(int i(a); i <= b; ++i)
#define FORD(i,a,b) for(int i(a); i >= b; --i)
#define REP0(i,n) FOR(i,0,n-1)
#define REP1(i,n) FOR(i,1,n)
#define PU push_back
#define PO pop_back
#define MP make_pair
#define A first
#define B second
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define SZ(s) (int)((s).size())
#define CL(a) memset((a),0,sizeof(a))
#define MAX(X,Y) X = max((X),(Y))
#define MIN(X,Y) X = min((X),(Y))
#define FORIT(X,Y) for(typeof((Y).begin()) X=(Y).begin(); X!=(Y).end(); ++X)
#define VI vector <int>
#define ll long long
#define PII pair<int,int>
#define PDD pair<double,double>
#define INF 1000000000

using namespace std;

bool check(string &s, map<char,int> &cnt) {
  map<char,bool> seen;
  map<char,int> c;
  char p = 0;
  REP0(i,SZ(s)) {
    if (s[i]!=p) {
      p=s[i];
      if (seen[p]) {
        return false;
      }
      seen[p]=true;
    }
    c[p]++;
  }
  FORIT(it,c) {
    if (it->A!=s[0]&&it->A!=s[SZ(s)-1])
      if (it->B!=cnt[it->A]) {
        return false;
      }
  }
  return true;
}
#define mod 1000000007
ll facc[101];
ll fac(int f) {
  if (f==0||f==1)
    return 1;
  else if (facc[f]!=0)
    return facc[f];
  ll ff = f*fac(f-1);
  if (ff >= mod)
    ff%=mod;
  facc[f] = ff;
  return ff;
}
bool comb1(vector<string> &S) {
  int n = SZ(S);
  REP0(i,n) {
    if (S[i][SZ(S[i])-1]!=S[i][0])
        continue;
    char p = S[i][0];
    REP0(j,n) {
      if (i==j)
        continue;
      if (S[j][0]==p) {
        S[i]+=S[j];
        S.erase(S.begin()+j);
        return true;
      }
    }
  }
  return false;
}
bool comb(vector<string> &S) {
  int n = SZ(S);
  REP0(i,n) {
    char p = S[i][SZ(S[i])-1];
    REP0(j,n) {
      if (i==j)
        continue;
      if (S[j][0]==p) {
        S[i]+=S[j];
        S.erase(S.begin()+j);
        return true;
      }
    }
  }
  return false;
}
int T;
void solve() {
  T++;
  printf("Case #%d: ", T);
  int N;
  cin >> N;
  vector<string> S(N);
  map<char,int> cnt;
  REP0(i,N) {
    cin >> S[i];
    REP0(j,SZ(S[i])) {
      cnt[S[i][j]]++;
    }
  }
  REP0(i,N) {
    if (!check(S[i],cnt)) {
      printf("0\n");
      return;
    }
  }
  SORT(S);
  FORIT(it,S) {
//    cout << *it << endl;
  }
//  cout << N << endl;
  // merge same char
  ll w = 1;
  int f=0;
  char p=0;
  vector<string> ss;
  REP0(i,N) {
    if (S[i][SZ(S[i])-1]!=p||S[i][0]!=p) {
      if (S[i][0]==S[i][SZ(S[i])-1])
        p=S[i][0];
      else
        p=0;
      ss.PU(S[i]);
      w*=fac(f);
      f=1;
    } else {
      ss[SZ(ss)-1]+=S[i];
      f++;
    }
  }
  w*=fac(f);
  FORIT(it,ss) {
//    cout << *it << endl;
  }
//  cout << w << endl;
  while (comb1(ss));
  while (comb(ss));
  string ff="";
  FORIT(it,ss) {
    ff+=*it;
//    cout << *it << endl;
  }
  w*=fac(SZ(ss));
  if (check(ff,cnt))
    cout << w << endl;
  else
    cout << 0 << endl;
}

int main() {
//  freopen("B.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
  return 0;
}
