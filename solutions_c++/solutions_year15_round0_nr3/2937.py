#include <bits/stdc++.h>

const int N = 10 * 1000;

int l, x, n;
char s[N + 1];

const int _u = 0, _i = 1, _j = 2, _k = 3, _mu = 4, _mi = 5, _mj = 6, _mk = 7;

int mtable[4][4] = {_u,  _i,  _j,  _k,
	_i, _mu,  _k, _mj,
	_j, _mk, _mu,  _i,
	_k,  _j, _mi, _mu};
int pm[N + 1] = {_u};

int multiply(int a, int b) {
	bool neg = false;
	if (a > _k) {
		a -= _mu;
		neg = !neg;
	}
	if (b > _k) {
		b -= _mu;
		neg = !neg;
	}
	int result = mtable[a][b];
	if (result > _k) {
		result -= _mu;
		neg = !neg;
	}
	return neg? result + _mu: result;
}

bool solve() {
	n = l * x;
	char ts[N + 1] = "";
	while (x--)
		strcat(ts, s);
	for (int i = 0; ts[i]; ++i)
		pm[i + 1] = multiply(pm[i], ts[i] - 'i' + _i);
	for (int i = 1; i < n; ++i)
		if (pm[i] == _i)
			for (int j = i + 1; j < n; ++j)
				if (multiply(_mu, multiply(pm[i], pm[j])) == _j &&
					multiply(_mu, multiply(pm[j], pm[n])) == _k)
					return true;
	return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int cnum = 1; cnum <= t; ++cnum) {
		scanf("%d %d %s", &l, &x, s);
		printf("Case #%d: %s\n", cnum, solve()? "YES": "NO");
	}
	//std::cout << clock() * 1000 / CLOCKS_PER_SEC << '\n';
	return 0;
}
