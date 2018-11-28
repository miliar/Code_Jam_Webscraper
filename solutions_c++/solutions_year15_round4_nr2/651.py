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

typedef long long LL;
typedef pair<int,int> PII;

const double eps = 0;

int N;
double V, X;
vector<pair<double, double> > vpdd;


int main() {
    freopen("C:\\Users\\dd\\Downloads\\B-small-attempt5.in", "r", stdin);
    freopen("C:\\Users\\dd\\Downloads\\B-small-attempt5.out", "w", stdout);

    int Te; cin >> Te;
    for (int te = 1; te <= Te; te ++) {

        cin >> N >> V >> X;
        vpdd.clear();
        for (int i = 0; i < N; i ++) {
            double r, c;
            cin >> r >> c;
            vpdd.push_back(make_pair(c, r));
        }
        sort(vpdd.begin(), vpdd.end());
        
        double ans;
        bool fail = false;
        if (N == 1) {
			if (vpdd[0].first != X) {
				fail = true;
			} else {
				ans = V / vpdd[0].second;
			}
		} else {
			if (vpdd[0].first == vpdd[1].first && vpdd[0].first == X) {
				ans = V / (vpdd[0].second + vpdd[1].second);
			} else if (vpdd[0].first == X) {
				ans = V / vpdd[0].second;
			} else if (vpdd[1].first == X) {
				ans = V / vpdd[1].second;
			} else if (vpdd[0].first < X && vpdd[1].first > X) {
				double v01 = 0.0f, v02 = V;
				while (v01 * (1.0 + 1e-12) < v02) {
					double mid = (v01 + v02) / 2;
					if (mid * vpdd[0].first + (V - mid) * vpdd[1].first < V * X) {
						v02 = mid;
					} else {
						v01 = mid;
					}
				}
				ans = max(v01 / vpdd[0].second, (V - v01) / vpdd[1].second);
			} else {
				fail = true;
			}
		}

        printf("Case #%d: ", te);
        if (fail) {
            puts("IMPOSSIBLE");
        } else {
            printf("%.17lf\n", ans);
        }
    }
    //system("pause");
}
