#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <functional>
#include <string>
#include <iostream>
#define ROCK 0
#define PAPER 1
#define SCISSOR 2
#define MX 5000
using namespace std;
int N, R, P, S;

int m[MX];

char convert(int i) {
	if (i == 0) return 'R';
	if (i == 1) return 'P';
	if (i == 2) return 'S';
}
string ans;
int loses[3] = { 2, 0, 1 };
void solve(int left, int right, int color) {
	int mid = (left + right) / 2;
	if (left == right) {
		m[left] = color;
		return;
	}
	solve(left, mid, color); solve(mid + 1, right, loses[color]);
}
void sort_string(int left, int right) {
	if (left == right) return;
	int mid = (left + right) / 2;
	sort_string(left, mid); sort_string(mid + 1, right);
	if (ans.substr(left, mid - left + 1) > ans.substr(mid+1, mid - left + 1)) {
		for (int i = left; i <= mid; i++) {
			swap(ans[i], ans[i + mid - left + 1]);
		}
	}
}
void testcase() {
	scanf("%d %d %d %d", &N, &R, &P, &S);
	
	ans = "";
	int n2 = 1 << N;
	for (int i = 0; i < 3; i++) {
		solve(0, (1<<N) - 1, i);
		
		int r = 0, p = 0, s = 0;
		for (int j = 0; j < (1 << N); j++) {
			if (m[j] == 0) r++;
			if (m[j] == 1) p++;
			if (m[j] == 2) s++;
		}
		if (R == r && P == p && S == s) {
			for (int j = 0; j < (1 << N); j++) {
				ans += string(1, convert(m[j]));
			}
			break;
		}
		
	}

	if (ans != "") {
		sort_string(0, (1<<N)- 1);
		cout << ans;
	}
	else {
		printf("IMPOSSIBLE");
	}
}


int main(void) {
	freopen("c:\\icpc\\a_l_input.txt", "r", stdin);
	freopen("c:\\icpc\\a_l_output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		testcase();
		printf("\n");
	}
}