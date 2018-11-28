#pragma comment(linker, "/STACK:50000000")
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, W, H;
int X1[1005], Y1[1005], X2[1005], Y2[1005], d[1005];

int main() {
    //freopen("x.in", "r", stdin);

	//freopen("C-small-attempt2.in", "r", stdin);
	//freopen("C-small-attempt2.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		cerr << tt << endl;
  		printf("Case #%d: ", tt);
		cin >> W >> H >> k;
		F0(i,k) cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
		int ans = W;

		for (int tt = 0; tt < 2; tt++) {
			if (tt == 1) {
				F0(i,k) {
					X1[i] = W - X1[i] - 1;
					X2[i] = W - X2[i] - 1;
					swap(X1[i], X2[i]);
				}
			}

			F0(i,k) {
				d[i] = X1[i];
			}
			int sg = 1;
			while (sg) {
				sg = 0;
				F0(i,k) F0(j,k) {
					int dx, dy;
					if (X1[i] > X2[j]) dx = X1[i]-X2[j]-1;
					else if (X1[j] > X2[i]) dx = X1[j]-X2[i]-1;
					else dx = 0;

					if (Y1[i] > Y2[j]) dy = Y1[i]-Y2[j]-1;
					else if (Y1[j] > Y2[i]) dy = Y1[j]-Y2[i]-1;
					else dy = 0;

					int dist = max(dx, dy);
					if (d[i] + dist < d[j]) {
						d[j] = d[i] + dist;
						sg = 1;
					}
				}
			}
			F0(i,k) ans = min(ans, d[i] + W-X2[i]-1);
		}
		cout << ans << endl;
	}
	//while (1);
	return 0;
}
