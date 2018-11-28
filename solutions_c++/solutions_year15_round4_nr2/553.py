#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long double ld;
typedef pair <ld, ld> ldld;

const ld mx = 1000000000000.0l;
const int Maxn = 105;
const int Maxt = 150;
const ld eps = 1e-17l;

int T;
int n;
ld V, X;
ldld CR[Maxn];

bool Ok(ld tim)
{
	ld lft = V, mxX = 0.0;
	bool ok = CR[n - 1].first >= X && tim * CR[n - 1].second >= V;
	for (int i = n - 1; i >= 0 && lft > eps; i--) {
		ld tk = min(lft, tim * CR[i].second); lft -= tk;
		mxX += tk * CR[i].first;
	}
	if (!ok && (lft > eps || mxX + eps < V * X)) return false;
	lft = V; ld mnX = 0.0;
	ok = CR[0].first <= X && tim * CR[0].second >= V;
	for (int i = 0; i < n && lft > 0.0l; i++) {
		ld tk = min(lft, tim * CR[i].second); lft -= tk;
		mnX += tk * CR[i].first;
	}
	return ok || lft <= eps && mnX <= V * X + eps;
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		cin >> n >> V >> X;
		for (int i = 0; i < n; i++)
			cin >> CR[i].second >> CR[i].first;
		printf("Case #%d: ", tc);
		if (n == 2 && CR[0].first == CR[1].first) { CR[0].second += CR[1].second; n--; }
		if (n == 1)
			if (X == CR[0].first) cout << fixed << setprecision(10) << V / CR[0].second << endl;
			else printf("IMPOSSIBLE\n");
		else {
			ld b = V * (X - CR[0].first) / (CR[1].first - CR[0].first);
			ld a = V - b;
			if (b + eps >= 0.0 && a + eps >= 0.0) cout << fixed << setprecision(10) << max(a / CR[0].second, b / CR[1].second) << endl;
			else printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}