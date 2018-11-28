#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <numeric>
#include <complex>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;
typedef long long ll;
const double EPS = 1e-9;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef vector<vector<int> > mat;
#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
#define pb push_back
#define mp make_pair
#define INF 1e+9


int main(void) {
	int T, A, B, K;
	cin >> T;
	for (int ca = 1; ca <= T; ca++) {
		cin >> A >> B >> K;
		ll ans = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				if ((i & j) < K) {
					ans++;
					//cout << i << " " << j << endl;
				}
				//cout << (i&j) << endl;
			}
		}
		cout << "Case #" << ca << ": " << ans << endl;
	}
}