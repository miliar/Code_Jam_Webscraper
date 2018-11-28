#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int T, n, a[1005], o[1005], ans;
bool b[1005];
bool f(int i, int j) {
	return a[i] < a[j];
}
int c[1005];
void add(int x, int a) {    // inc [x] by a
  for (int i=x; i<1003; i+=i&(-i)) c[i] += a;}
int sum(int x) {    // return sum[1..x]
  int ret = 0;
  for (int i=x; i>0; i-=i&(-i)) ret += c[i];
  return ret;
}


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &n);
		int ma = 0;
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &a[i]);
			ma = max(ma, a[i]);
			o[i] = i;
			b[i] = true;
		}
		sort(o + 1, o + 1 + n, f);
		memset(c, 0, sizeof c);
		ans = 0;
		int le = 1, ri = n;
		/*for (int i = 1; i <= n; ++i) {
			if (b[o[i]]) {
				int dl = o[i] - le - ;
				int dr = ri - o[i]
			}
		}*/
		for (int i = 1; i <= n; ++i) {
			int mi = ma+1, mii = -1;
			for (int j = le; j <= ri; ++j) {
				if (a[j] < mi) {
					mi = a[j];
					mii = j;
				}
			}
			int dl = mii - le;
			int dr = ri - mii;
			if (dl < dr) {
				ans += dl;
				for (int j = mii; j > le; --j) {
					swap(a[j-1], a[j]);
				}
				le++;
			}
			else {
				ans += dr;
				for (int j = mii; j < ri; ++j) {
					swap(a[j], a[j+1]);
				}
				ri--;
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
