#include <cstdio>
#include <vector>
#include <cstring>
#include <map>

using namespace std;

char s[100][100];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		printf("Case #%d: ", t);
		int n, m;
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++)
			scanf("%s\n", s[i]);
		int nm = 1;
		for (int i = 0; i < m; i++)
			nm *= n;
		int max = 0, spos = 0;
		for (int x = 0; x < nm; x++) {
			int tmp = x;
			vector<int> a[5];
			for (int i = 0; i < m; i++) {
				a[tmp % n].push_back(i);
				tmp /= n;
			}
			int anan = 0;
			for (int i = 0; i < n; i++) {
				if (a[i].empty()) continue;
				map<char, int> to[100];
				int all = 1;
				for (int j = 0; j < (int)a[i].size(); j++) {
					int len = strlen(s[a[i][j]]);
					int cur = 0;
					for (int k = 0; k < len; k++) {
						char ch = s[a[i][j]][k];
						if (!to[cur].count(ch)) {
							to[cur][ch] = all;
							cur = all++;
						}
						else {
							cur = to[cur][ch];
						}
					}
				}
				anan += all;
			}
			if (anan > max) {
				max = anan;
				spos = 1;
			}
			else
				if (anan == max)
					spos++;
		}
		printf("%d %d\n", max, spos);
	}
	return 0;
}
