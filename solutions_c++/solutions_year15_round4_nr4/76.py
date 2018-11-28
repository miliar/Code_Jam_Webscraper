#include <cstdio>

const int MAX = 110, MOD = 1000000007;

typedef long long ll;

int r, c;

//save[R][k][t]: row R까지 만듦. t=0이면 3 써야 하고 t=1이면 2 써야 한다.
//k=0 1 k=1 3 k=2 4 k=3 6 k=4 12
int save[MAX][5][2], lcs[] = { 1, 3, 4, 6, 12 };

void update(int &target, ll val) {
	target = (target + val) % MOD;
}

int findIndex(int a, int b) {
	int i;
	for(i = 0; i < 5; i++) {
		if(lcs[i]%a == 0 && lcs[i]%b == 0)
			return i;
	}
}

//b에서 시작
ll findMul(int a, int b) {
	int lcm = lcs[findIndex(a, b)];
	if(lcm != b) {
		return a * b / lcm;
	}

	return a;
}

void solve() {
	int i, j;
	for(i = 0; i <= r; i++) {
		for(j = 0; j < 5; j++) {
			save[i][j][0] = save[i][j][1] = 0;
		}
	}

	save[0][0][0] = 1;
	save[0][0][1] = 1;

	for(i = 0; i <= r; i++) {
		for(j = 0; j < 5; j++) {
			int index;
			ll mul;

			//3 3 3
			//3 3 3
			update(save[i+2][j][1], save[i][j][0]);

			//2 2 2
			update(save[i+1][j][0], save[i][j][1]);

			if(c%3 == 0) {
				//1 2 2
				//1 2 2
				index = findIndex(3, lcs[j]);
				mul = findMul(3, lcs[j]);
				update(save[i+2][index][0], save[i][j][1]*mul);
			}

			if(c%6 == 0) {
				//1 1 2 2 2 2
				//2 2 2 1 1 2
				index = findIndex(6, lcs[j]);
				mul = findMul(6, lcs[j]);
				update(save[i+2][index][0], save[i][j][1]*mul);
			}

			if(c%4 == 0) {
				//1 2 2 2
				//1 2 1 2
				//2 2 1 2
				index = findIndex(4, lcs[j]);
				mul = findMul(4, lcs[j]);
				update(save[i+3][index][0], save[i][j][1]*mul);
			}
		}
	}
}

int main() {
	freopen("D.out", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);

	for(nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%d%d", &r, &c);

		solve();

		int ans = 0;
		int i, j;
		for(i = 0; i < 5; i++) {
			update(ans, save[r][i][0]);
			update(ans, save[r][i][1]);
		}

		printf("Case #%d: %d\n", nowCase, ans);
	}

	return 0;
}