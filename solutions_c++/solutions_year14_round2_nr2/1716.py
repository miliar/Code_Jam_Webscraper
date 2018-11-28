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

  /*
  int T; cin >> T;
  for(int t = 0; t < T; ++t) {
    int N; cin >> N;
    string s1, s2; cin >> s1 >> s2;
    int cnt1[26] = {0}, cnt2[26] = {0};
    for(int i = 0; i < s1.length(); ++i) cnt1[s1[i]-'a']++;
    for(int i = 0; i < s2.length(); ++i) cnt2[s2[i]-'a']++;
    int res = 0;
    for(int i = 0; i < 26; ++i) {
      if((!cnt1[i] && cnt2[i]) || (!cnt2[i] && cnt1[i])) {
	cout << "Case #" << t+1 << ": Felga Won\n";
	goto HELL;
      }
      res += ABS(cnt1[i] - cnt2[i]);
    }
    cout << "Case #" << t+1 << ": " << res << '\n';
    HELL:;
  }
  */

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

  return 0;
}
