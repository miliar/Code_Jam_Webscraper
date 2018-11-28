#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int MAXN = 1e5 + 5;

int tt, n, R, S, P;
char sol[MAXN];

void dfs(int curr, int n, int& R, int& P, int& S, char winner) {
	if (curr == n) {
		switch (winner) {
		case 'R':
			R--;
			break;
		case 'P':
			P--;
			break;
		case 'S':
			S--;
			break;
		}
	} else {
		switch (winner) {
		case 'R':
			dfs(curr + 1, n, R, P, S, 'R');
			dfs(curr + 1, n, R, P, S, 'S');
			break;
		case 'P':
			dfs(curr + 1, n, R, P, S, 'P');
			dfs(curr + 1, n, R, P, S, 'R');
			break;
		case 'S':
			dfs(curr + 1, n, R, P, S, 'S');
			dfs(curr + 1, n, R, P, S, 'P');
			break;
		}	
	}
}

bool ok(char winner, int n, int R, int P, int S) {
	dfs(0, n, R, P, S, winner);
	return (R == 0 && P == 0 && S == 0);
}

void make_any(int curr, int n, char winner, int l, int r) {
	if (curr == n) {
		sol[l] = winner;
		return;
	}
	int mid = (l + r) / 2;
	switch (winner) {
	case 'R':
		make_any(curr + 1, n, 'R', l, mid);
		make_any(curr + 1, n, 'S', mid + 1, r);
		break;
	case 'P':
		make_any(curr + 1, n, 'P', l, mid);
		make_any(curr + 1, n, 'R', mid + 1, r);
		break;
	case 'S':
		make_any(curr + 1, n, 'P', l, mid);
		make_any(curr + 1, n, 'S', mid + 1, r);
		break;
	}	
}

bool compare(int l1, int r1, int l2, int r2) {
	for (int i1 = l1, i2 = l2; i1 <= r1 && i2 <= r2; i1++, i2++) {
		if (sol[i1] < sol[i2]) return false;
		if (sol[i1] > sol[i2]) return true;
	}
	return false;
}

void change(int l1, int r1, int l2, int r2) {
	for (int i1 = l1, i2 = l2; i1 <= r1 && i2 <= r2; i1++, i2++) {
		swap(sol[i1], sol[i2]);
	}
}

void sort_sol(int curr, int n, int l, int r) {
	if (curr == n)
		return;
	int mid = (l + r) / 2;
	if (compare(l, mid, mid + 1, r)) {
		change(l, mid, mid + 1, r);
	}
	sort_sol(curr + 1, n, l, mid);
	sort_sol(curr + 1, n, mid + 1, r);
}

int main() {
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
    	scanf("%d %d %d %d", &n, &R, &P, &S);
    	if (ok('R', n, R, P, S)) {
    		make_any(0, n, 'R', 0, (1 << n) - 1);
    		sort_sol(0, n, 0, (1 << n) - 1);
    		printf("Case #%d: ", t);
    		for (int i = 0; i < (1 << n); i++) printf("%c", sol[i]);
    		printf("\n");
    	} else if (ok('P', n, R, P, S)) {
    		make_any(0, n, 'P', 0, (1 << n) - 1);
    		sort_sol(0, n, 0, (1 << n) - 1);
    		printf("Case #%d: ", t);
    		for (int i = 0; i < (1 << n); i++) printf("%c", sol[i]);
    		printf("\n");
    	} else if (ok('S', n, R, P, S)) {
    		make_any(0, n, 'S', 0, (1 << n) - 1);
    		sort_sol(0, n, 0, (1 << n) - 1);
    		printf("Case #%d: ", t);
    		for (int i = 0; i < (1 << n); i++) printf("%c", sol[i]);
    		printf("\n");
    	} else {
    		printf("Case #%d: IMPOSSIBLE\n", t);
    	}
    }
    return 0;
}
