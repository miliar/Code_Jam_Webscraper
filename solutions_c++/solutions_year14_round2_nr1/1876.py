#include <iostream>
#include <cstdio>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <climits>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <cctype>
#include <bitset>
#include <ctime>
#include <cassert>
#include <fstream>
#include <complex>
#include <iomanip>
using namespace std;

#define MIN(x,y) (((x)<(y))?(x):(y))
#define MAX(x,y) (((x)>(y))?(x):(y))
#define ABS(x) (((x)<0)?(-(x)):(x))
#define ff first
#define ss second
#define ei else if
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ull, ull> puu;
typedef pair<int,pair<int,int> > piii;
const ld EPS = 1e-7;
const ld PI  = 3.141592653589793;

int main() {
  ios_base::sync_with_stdio(0);

  int T; cin >> T;
  for(int t = 0; t < T; ++t) {
    int N; cin >> N;
    string s1, s2; cin >> s1 >> s2;
    int p1 = 0, p2 = 0; char c1 = s1[0], c2 = s2[0];
    int d1 = 0, d2 = 0;
    int res = 0;
    while(1) {
      d1 = d2 = 0;
      if(p1 == s1.length() && p2 == s2.length())
	break;

      c1 = s1[p1], c2 = s2[p2];
      if(c1 != c2) {
	cout << "Case #" << t+1 << ": Fegla Won\n";
	goto HELL;
      }

      if(p1 != s1.length()) {
	while(s1[p1] == c1) {p1++; d1++;}
      }
      if(p2 != s2.length()) {
	while(s2[p2] == c2) {p2++; d2++;}
      }
      res += ABS(d1 - d2);
    }
    cout << "Case #" << t+1 << ": " << res << '\n';
    HELL:;
  }

  /*
  int T; cin >> T;
  for(int t = 1; t <= T; ++t) {
    int A, B, K; cin >> A >> B >> K;
    ll res = 0;
    for(int i = 0; i < A; ++i)
      for(int j = 0; j < B; ++j)
	if((i & j) < K) {
		  res++;
		  //cout << i << ' ' << j << '\n';
	}
    cout << "Case #" << t << ": " << res << '\n';
}
  */

  return 0;
}
