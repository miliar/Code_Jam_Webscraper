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
	int t, a[16], b[16], f, s, tmp, ret = 0;
	cin >> t;
	for (int casenum = 1; casenum <= t; casenum++) {
		ret = 0;
		cin >> f;
		int ans[4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a[i];
				if (i + 1 == f) ans[j] = a[i];
			}
		}

		cin >> s;
		tmp = 0;
		int ans1;	
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> b[i];
				if (i + 1 == s){
					for (int k = 0; k < 4; k++) {
						if (ans[k] == b[i]){
							ret++;
							ans1 = b[i];
						}
					}
				}
			}
		}
		printf("Case #%d: ", casenum);
		if (ret == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (ret == 1) {
			cout << ans1 << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}