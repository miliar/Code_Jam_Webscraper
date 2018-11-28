#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

char S[23333];

int main(void)
{
	int TK = 0;
	int T = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++TK);

		scanf("%s", S);
		int n = strlen(S);

		vector<pii> vp;
		int last = -1;
		int cnt = 0;
		for (int i = 0;i <= n;i++) {
			if (S[i] == last) {
				cnt++;
			} else {
				if (last != -1) vp.emplace_back(last, cnt);
				last = S[i];
				cnt = 1;
			}
		}

		int ans = 0;
		while (true) {
			vector<pii> vpc;
			// puts("-----");
			for (auto x: vp) {
				// printf("%d %d\n", x.first, x.second);
				ans += x.second / 2 * 10;
				x.second %= 2;
				if (x.second) {
					if (vpc.size() && vpc[vpc.size()-1].first == x.first)
						vpc[vpc.size()-1].second += x.second;
					else vpc.push_back(x);
				}
			}
			// puts("-----");
			if (vp == vpc) break;
			vp = vpc;
		}
		// printf("??%d??\n",ans);
		ans += vp.size() / 2 * 5;
		printf("%d\n", ans);
	}
	return 0;
}