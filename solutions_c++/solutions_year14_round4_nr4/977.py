#include <cstdio>
#include <string>
#include <set>
#include <algorithm>
using namespace std;
const int MOD = 1000000007;
string str[20];
set<string> s[10], tmp;
int main() {
	int testnum, m, n, way, ans, ansc, tans;
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		scanf("%d%d", &m, &n);
		char S[20];
		for (int i = 0;i < m;i++) {
			scanf("%s", S);
			str[i] = S;
		}
		way = 1;
		ans = ansc = 0;
		for (int i = 0;i < m;i++) way *= n;
		for (int i = way - 1;i >= 0;i--) {
			for (int j = 0;j < n;j++) s[j].clear();
			int temp = i;
			for (int j = 0;j < m;j++) {
				s[temp % n].insert(string(str[j]));
				temp /= n;
			}
			bool suc = true;
			for (int j = 0;j < n;j++) {
				if (s[j].size() == 0) {
					suc = false;
					break;
				}
			}
			if (!suc) continue;
			tans = 0;
			for (int j = 0;j < n;j++) {
				tmp.clear();
				for (set<string>::iterator it = s[j].begin();it != s[j].end();it++) {
					for (int k = 0;k < it->length();k++) {
						tmp.insert(it->substr(0, k + 1));
					}
				}
				tans += tmp.size() + 1;
			}
			if (tans > ans) {
				ans = tans;
				ansc = 1;
			} else if (tans == ans) {
				ansc++;
			}
		}
		printf("Case #%d: %d %d\n", test, ans, ansc);
	}
	return 0;
}
