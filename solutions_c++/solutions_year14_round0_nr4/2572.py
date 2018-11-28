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

int main(void)
{
	int T, n;
	double tmp;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		vector<double> N, K;
		cin >> n;
		for (int j = 0; j < n; j++) {
			cin >> tmp;
			N.pb(tmp);
		}
		for (int j = 0; j < n; j++) {
			cin >> tmp;
			K.pb(tmp);
		}
		sort(N.begin(), N.end());
		sort(K.begin(), K.end());
		int naomi = 0, ken = 0, ans1 = 0, ans2 = 0;
		while (1) {
			if (naomi == n) break;
			if (N[naomi] < K[ken]) {
				naomi++;
			} else {
				ans1++;
				naomi++;
				ken++;
			}
		}
		naomi = 0;
		ken = 0;
		while (1) {
			if (ken == n) break;
			if (N[naomi] > K[ken]) {
				ken++;
			} else {
				ans2++;
				naomi++;
				ken++;
			}
		}

		printf("Case #%d: %d %d\n", i, ans1, n - ans2);
	}
	return 0;
}