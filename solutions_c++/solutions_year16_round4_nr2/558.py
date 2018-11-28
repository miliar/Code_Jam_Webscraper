#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
const int N = 205;
double f[N], a[N];
int n, k, h;
double solve(int p) {
	for (int i=1; i<=k; ++i) f[i] = 0;
	f[0] = 1;
	for (int i=1; i<=p; ++i) {
		for (int j=k; j; --j)
			f[j] = f[j-1] * a[i] + f[j] * (1 - a[i]);
		f[0] *= (1 - a[i]);
	}
	for (int i=n-(k-p)+1; i<=n; ++i) {
		for (int j=k; j; --j)
			f[j] = f[j-1] * a[i] + f[j] * (1 - a[i]);
		f[0] *= (1 - a[i]);	
	}
	return f[h];
}
void run() {
	double ans = 0;
	scanf("%d%d", &n, &k); h = k / 2;
	for (int i=1; i<=n; ++i)
		scanf("%lf", a + i);
	sort(a + 1, a + n + 1);
	for (int i=0; i<=k; ++i)
		ans = max(ans, solve(i));
	printf("%.10lf\n", ans);
}
int main() {
	int T; scanf("%d", &T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}