#include <iostream>
using namespace std;
int main() {
	int T, t;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		int N;
		scanf("%d", &N);
		string S;
		cin >> S;
		int ans = 0;
		int standing_already = S[0] - '0';
		for (int i = 1; i < S.length(); i++) {
			if (i > standing_already) {
				ans += (i - standing_already);
				standing_already = i;
			}
			standing_already += S[i] - '0';
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}