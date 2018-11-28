#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int T; cin >> T; for (int t=1; t<=T; ++t) {
		int n; int p[1002]; string S;

		cin >> n >> S;

		for (int i=0; i<=n; ++i)
			p[i] = S[i] - '0';

		printf("Case #%d: ", t);
		int ret = 0;

		int SUM = 0;
		for (int i=0; i<=n; ++i) {
			if (i && p[i] && i > SUM) {
				int obj = i - SUM;

				for (int j=i-1; j>=0; --j) {
					if (p[j] < 9) {
						int plus = min(9 - p[j], obj);
						obj -= plus;
						p[i] += plus;
						ret += plus;
					}

					if (obj <= 0)
						break;
				}
			}
			SUM += p[i];
		}

		printf("%d", ret);
		puts("");
	}
}