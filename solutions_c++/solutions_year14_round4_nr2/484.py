#include <cstdio>
#include <algorithm>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template<typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0'; ch=getchar());
	for (; ch>='0'; ch=getchar()) x = x*10+ch-'0';
}
const int N = 100005;
int n, a[N], p[N], c[N];
inline bool cmp(int x, int y) {return a[x] < a[y];}
inline void A(int w, int x) {
	for (; w<=n; w+=w&-w) c[w] += x;
}
inline int Q(int w) {
	int s = 0;
	for (; w; w-=w&-w) s += c[w];
	return s;
}
void run() {
	R(n);
	for (int i=1; i<=n; ++i) R(a[i]), p[i] = i, A(i, 1);
	sort(p+1, p+n+1, cmp);
	int ans = 0, t;
	for (int i=1; i<=n; ++i) {
		A(p[i], -1);
		t = Q(p[i]);
		ans += min(n-i-t, t);
	}
	printf("%d\n", ans);
}
int main() {
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}
