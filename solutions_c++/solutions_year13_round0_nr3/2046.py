#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

vector<long long> pre;

template<class T, class U> T get(U x) {
  stringstream ss;
  T y;
  ss << x;
  ss >> y;
  return y;
}

int is_palindrome(long long x) {
  string A = get<string>(x);
  string B = A; reverse(B.begin(),B.end());
  return A == B;
}

int main() {
  // 1 -> 7 digits
  pre.push_back(1), pre.push_back(4), pre.push_back(9);
  for(int i=1;i<=999;i++) {
    int nd=(i<10?1:(i<100?2:3));
    string A = get<string>(i), B = A; reverse(B.begin(),B.end());
    for(int j=0;j<10;j++) {
      string C = get<string>(j);
      long long z = get<long long>(A+C+B);
      z = z*z;
      if(is_palindrome(z)) pre.push_back(z);
    }
    long long z = get<long long>(A+B);
    z = z*z;
    if(is_palindrome(z)) pre.push_back(z);
  }
  int T; cin>>T;
  for(int testcase=1;testcase<=T;testcase++) {
    long long A,B;
    cin>>A>>B;
    int ct=0;
    rep(i,pre.size()) if(A<=pre[i]&&pre[i]<=B) ct++;
    printf("Case #%d: %d\n",testcase,ct);
  }
  return 0;
}

