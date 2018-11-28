#include <iostream>
using namespace std;

int N;
int num[1010];

void input() {
	scanf("%d", &N);
	for(int i = 0; i < N; ++i) scanf("%d", &num[i]);
}

int solve1() {
	int ans = 0;
	for(int i = 1; i < N; ++i) {
		if(num[i] < num[i-1]) ans += (num[i-1] - num[i]);
	}
	return ans;
}

int solve2() {
	int eatRate = 0, tpRate;
	for(int i = 1; i < N; ++i) {
		tpRate = num[i - 1] - num[i];
		if(tpRate > 0 && tpRate > eatRate) eatRate = tpRate;
	}

	int ans = 0;
	for(int i = 0; i < N - 1; ++i) {
		if(num[i] >= eatRate) ans += eatRate;
		else ans += num[i];
	}	
	return ans;
}

void solve() {
	int ans1 = solve1();
	int ans2 = solve2();
	printf("%d %d\n", ans1, ans2);
}


int main() {
	//freopen("c:/aaa.txt", "r", stdin);
	freopen("c:/A-large.in", "r", stdin);
	freopen("c:/A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int ca = 0; ca < T; ++ca) {
		printf("Case #%d: ", ca + 1);
		input();
		solve();
	}
	return 0;
}