#include <bits/stdc++.h>

using namespace std;

const char E = 1;
const char I = 2;
const char J = 3;
const char K = 4;

inline char sign(char a) {
	return a < 0 ? -1 : 1;
}

inline int multiply(char a, char b) {
	char sgn = sign(a) * sign(b);
	a = abs(a);
	b = abs(b);
	if (a == E || b == E)
		return sgn * a * b;
	if (a == b)
		return -sgn;
	if (a == I) {
		if (b == J)	return sgn * K;
		else if (b == K) return -sgn * J;
	}
	else if (a == J) {
		if (b == I)	return -sgn * K;
		else if (b == K) return sgn * I;
	}
	else if (a == K) {
		if (b == I)	return sgn * J;
		else if (b == J) return - sgn * I;
	}
	exit(42);
}

inline int divide(char a, char c) {
	char aa = abs(a);
	char cc = abs(c);
	char sgn = sign(a) * sign(c);
	if (aa == E) return sgn * cc;
	if (aa == cc) return sgn * E;
	if (cc == E) return -sgn * aa;
	if (aa == I) {
		if (cc == K) return sgn * J;
		else if (cc == J) return -sgn * K;
	}
	else if (aa == J) {
		if (cc == K) return - sgn * I;
		else if (cc == I) return sgn * K;
	}
	else if (aa == K) {
		if (cc == J) return sgn * I;
		else if (cc == I) return - sgn * J;
	}
	exit(43);
}

const int MAXN = 10000;
char s[MAXN+1], p[MAXN+1];

inline char getIntervale(int a, int b) {
	if (a == 0)
		return s[b];
	return divide(s[a-1], s[b]);
}

inline char convert(char c){
	if (c == 'i') return I;
	if (c == 'j') return J;
	if (c == 'k') return K;
	return E;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, x;
		scanf("%d%d", &n, &x);
		scanf("%s", p);
		for (int i = 0; p[i]; i++)
			p[i] = convert(p[i]);

		strcpy(s, "");
		while (x--) strcat(s, p);

		int d = strlen(s);
		for (int i = 1; i < d; i++)
			s[i] = multiply(s[i-1], s[i]);

		bool found = false;
		for (int i = 0; !found && i < d; i++) {
			if (s[i] != I) continue;
			for (int j = i+1; !found && j < d; j++) {
				if (getIntervale(i+1, j) == J && getIntervale(j+1, d-1) == K) {
					found = true;
				}
 			}
		}
		if (found)
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
}