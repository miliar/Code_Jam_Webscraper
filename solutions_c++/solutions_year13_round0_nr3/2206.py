#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
typedef  long long   ll;


#define ALL(x)   (x).begin(),(x).end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);




template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}

bool palin(ll a) {
  int arr[20], si = 0;
  while (a) {
    arr[si++] = a%10LL; a /= 10LL;
  }
  for (int i = 0; i < si/2; ++i) {
    if (arr[i] != arr[si-1-i]) return false;
  }
  return true;
}
vector<string> allpals;

void push(string s) {
  int si = s.size();
  for (int i = si-1; i >= 0; --i) s = s + s[i];
  allpals.PB(s);
}
void push0(string s) {
  int si = s.size();
  s = s + "0";
  for (int i = si-1; i >= 0; --i) s = s + s[i];
  allpals.PB(s);
}
void push1(string s) {
  int si = s.size();
  s = s + "1";
  for (int i = si-1; i >= 0; --i) s = s + s[i];
  allpals.PB(s);
}
void push2(string s) {
  int si = s.size();
  s = s + "2";
  for (int i = si-1; i >= 0; --i) s = s + s[i];
  allpals.PB(s);
}

bool LT(string &f, string &s) {
  if (f.size() < s.size()) return true;
  if (f.size() > s.size()) return false;
  return f < s;
}

string add(string s1, string s2) {
  string res;
  int carry = 0;
  for (int i = 0; i < max(s1.size(), s2.size()); ++i) {
    int s1i, s2i;
    if (i < s1.size()) s1i = s1[i]-'0'; else s1i = 0;
    if (i < s2.size()) s2i = s2[i]-'0'; else s2i = 0;

    int s = s1i + s2i + carry;
    carry = s / 10;
    s %= 10;
    res = res + char('0'+s);
  }
  if (carry) {
    res = res + char('0'+carry);
  }
  return res;
}

string multiply(string s1, string s2) {
  reverse(s1.begin(), s1.end());
  reverse(s2.begin(), s2.end());
  string res = "0";

  string sum[4];
  sum[0] = "0";
  for (int i = 1; i < 4; ++i) sum[i] = add(sum[i-1], s1);

  for (int j = 0; j < s2.size(); ++j) {
    // calculamos fila...
    string row = string(j, '0') + sum[s2[j]-'0']  ;
    res = add(res, row);
  }
  reverse(res.begin(), res.end());
  return res;
}


int main() {
  int i,j , k;
  allpals.PB("1");
  allpals.push_back("2");
  allpals.push_back("3");
  //cout << multiply("11", "11") << endl;
  for (int i1 = 50; i1 >= 1; --i1) {
    // arranca con 1.
    string a(i1, '0');
    a[0] = '1';
    push(a);
    push0(a);
    push1(a);
    push2(a);

    for (int i2 = 1; i2 < i1; ++i2) {
      a[i2] = '1';
      push(a);
      push0(a);
      push1(a);
      // recurse :S
      for (int i3 = i2+1; i3 < i1; ++i3) {
        a[i3] = '1';
        push(a);
        push0(a);
        push1(a);
        for (int i4 = i3+1; i4 < i1; ++i4) {
          a[i4] = '1';
          push(a);
          push0(a);
          push1(a);
          a[i4] = '0';
        }
        a[i3] = '0';
      }
      a[i2] = '0';
    }
    a[0] = '2';
    push(a);
    push0(a);
    push1(a);
  } 
  vector<string> aux = allpals;
  allpals.clear();
  for (i = 0; i < aux.size(); ++i) {
    if (aux[i].size() > 51) continue;
    string m = multiply(aux[i], aux[i]);
    if (m.size() > 100) continue;
    allpals.PB(m);
  }

  int casos; cin >> casos;
  for (int h = 0; h < casos; ++h) {
    string A, B; cin >> A >> B;
    int res = 0;
    for (i = 0; i < allpals.size(); ++i) {
      if (LT(allpals[i], B) or B == allpals[i]) res++;
      if (LT(allpals[i], A)) res--;
    }
    cout << "Case #" << h+1 << ": " << res << endl;
  } 
  return 0;
}
