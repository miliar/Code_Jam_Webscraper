#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 1010;
int a[N];

int b[N];
int n;

int cal(int mc) {
	int ret = 0;
	rep(i, mc) {
		int mx = -1; int pos = -1;
		rep(j, mc - i) {
			if (a[j] > mx) {
				mx = a[j];
				pos = j;
			}
		}
		for (int j = pos; j < mc - i - 1; ++j) {
			swap(a[j], a[j + 1]);
			++ret;
		}
	}
	int k = 0;
	for (int i = mc + 1; i < n; ++i) {
		int mx = -1; int pos = -1;
		for (int j = mc + k + 1; j < n; ++j) {
			if (a[j] > mx) {
				mx = a[j];
				pos = j;
			}
		}
		for (int j = pos; j > mc + k + 1; --j) {
			swap(a[j], a[j - 1]);
			++ret;
		}
		++k;
	}
	//rep(i, n) cout << a[i] << " "; cout << endl;
	//cout<<ret<<endl;
	return ret;
}
int c[1010];
int bru() {
	rep(i, n) c[i] = b[i];
	sort(b, b + n);
	int ret = inf;
	do {
		int up = 0;
		bool ok = 1;
		Rep(i, n - 2) {
			if (b[i] < b[i - 1] && b[i] < b[i + 1]) {
				ok = 0;
				break;
			}
		}
		if (!ok)continue;
		//rep(i, n) cout << b[i] << " "; cout << endl;
		rep(i, n) a[i] = c[i];
		//rep(i, n) cout << a[i] << " "; cout << endl;
		int cc = 0;
		rep(i, n) {
			int now = i;
			if (a[i] != b[i]) {
				for (int j = i + 1; j < n; ++j) {
					if (a[j] == b[i]) {
						for (int k = j; k > i; --k) {
							swap(a[k], a[k - 1]);
							++cc;
						}
						break;
					}
				}
			}
		}
		ret = min(ret, cc);
		//if (ret == 5) rep(i, n) cout << b[i] << " ";cout<<endl;
	} while (next_permutation(b, b + n));
	return ret;
}
int main() {
#if 1
	//freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large-ans.txt", "w", stdout);
#endif
	int T, ca = 1;
	
	for (scanf("%d", &T); T--; ) {
		cerr<<T<<endl;
		scanf("%d", &n);
		rep(i, n) scanf("%d", &a[i]);
		rep(i, n) b[i] = a[i];
		rep(i, n) c[i] = a[i];
		sort(c, c + n);
		int l = 0, r = n - 1;
		int ret = 0;
		rep(i, n) {
			rep(j, n) if (a[j] == c[i]) {
				if (j - l < r - j) {
					for (int k = j; k >= l + 1; --k) {
						swap(a[k], a[k - 1]);
						++ret;
					}
					++l;
				} else {
					for (int k = j; k <= r - 1; ++k) {
						swap(a[k], a[k + 1]);
						++ret;
					}
					--r;
				}
				break;
			}
		}
		//rep(i, n) cout << a[i] << " "; cout << endl;
		printf("Case #%d: %d\n", ca++, ret);
		//cout<<bru()<<endl;
		//if (ret != bru()) cout << "kk"<<endl;
	}
	return 0;
}



