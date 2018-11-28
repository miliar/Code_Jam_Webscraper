#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
using vi = vector<int>;
using vvi = vector<vi>;
using vd = vector<double>;
using vb = vector<bool>;

#define FU(i, a, b) for (remove_const_t<remove_reference_t<decltype(b)>> i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (auto i = (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)

#define all(V) (V).begin(), (V).end()
#define rall(V) (V).rbegin(), (V).rend()

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(b, e) TRACE({for (auto it = b; it != e; it++) cout << *it << " "; cout << endl;})
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR((V).begin(), (V).end());})

int cmp(double x, double y = 0., double tol = 1.e-8) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

ll mod(ll a, ll b) {
	return ((a%b)+b)%b;
}

char buf[1010];
void doit() {
	int K;
	scanf(" %s %d", buf, &K);
	int N = strlen(buf);

	int ans = 0;
	for (int i = 0; i + K <= N; i++) if (buf[i] == '-') {
		ans++;
		for (int j = i; j < i + K; j++) buf[j] = '+' + '-' - buf[j];
	}

	fu(i, N) if (buf[i] == '-') {
		printf(" IMPOSSIBLE\n");
		return;
	}
	printf(" %d\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	fu(t, T) {
		printf("Case #%d:", t+1);
		doit();
	}
	return 0;
}
