#include "bits/stdc++.h"
using namespace std;
int N;
int cnt[2501];
string str[100];
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.text", "w", stdout);
	int Case;
	cin >> Case;
	for (int tc = 1; tc <= Case; tc++) {
		cin >> N;
		int in;
		for (int i = 0; i < N * 2 - 1; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &in);
				cnt[in]++;
			}
		}
		printf("Case #1:");
		for (int i = 1; i <= 2500; i++)
			if (cnt[i] & 1)
				printf(" %d", i);
		printf("\n");
	}
	return 0;
}