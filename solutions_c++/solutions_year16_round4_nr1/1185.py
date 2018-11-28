#include <bits/stdc++.h>
using namespace std;


int n_test;
int n, p, r, s;

char mov[1<<12];

bool attempt(int i, int pos, char winner, bool counted = true) {
	mov[pos] = winner;
	if (counted) {
		if (winner == 'P') --p;
		if (winner == 'S') --s;
		if (winner == 'R') --r;
	}

	if (p < 0 || s < 0 || r < 0) 
		return false;

	if (i > n)
		return true;
	
	bool result;
	if (winner == 'P') 
		result = attempt(i + 1, pos, winner, false) && attempt(i + 1, pos + (1 << (n-i)), 'R');
	else if (winner == 'R')
		result = attempt(i + 1, pos, winner, false) && attempt(i + 1, pos + (1 << (n-i)), 'S');
	else if (winner == 'S')
		result = attempt(i + 1, pos, winner, false) && attempt(i + 1, pos + (1 << (n-i)), 'P');

	for (int j = 0; j < (1 << (n-i)); ++j)
		if (mov[pos + (1 << (n-i)) + j] < mov[pos + j]) {
			for (int j = 0; j < (1 << (n - i)); ++j)
				swap(mov[pos + j], mov[pos + (1 << (n-i)) + j]);
			break;
		} else if (mov[pos + (1 << (n-i)) + j] > mov[pos + j])
			break;
	return result;
}

void output() {
	for (int i = 0; i < (1<<n); ++i)
		printf("%c", mov[i]);
	printf("\n");
}

int main() { 
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &n_test);
	for (int test = 1; test <= n_test; ++test) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		int _r = r, _p = p, _s = s;

		printf("Case #%d: ", test);

		r = _r; p = _p, s = _s;
		if (attempt(1, 0, 'P')) {
			if (r == 0 && p == 0 && s == 0) {
				output();
				continue;
			}
		}
		r = _r; p = _p, s = _s;
		if (attempt(1, 0, 'R')) {
			if (r == 0 && p == 0 && s == 0) {
				output();
				continue;
			}
		}
		r = _r; p = _p, s = _s;
		if (attempt(1, 0, 'S')) {
			if (r == 0 && p == 0 && s == 0) {
				output();
				continue;
			}
		}
		
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
