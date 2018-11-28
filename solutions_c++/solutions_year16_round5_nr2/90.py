#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
const int N(111);
vector<int> sons[N];
int deg[N], a[N], cnt[N], c[N];
char st[N], tmp[N];
string s[N], cl[N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n;
		scanf("%d", &n);
		for(int i(0); i <= n; i++) {
			sons[i].clear();
		}
		for(int i(0); i <= n; i++) {
            deg[i] = 0;
		}
		for(int i(1); i <= n; i++) {
			scanf("%d", &a[i]);
			sons[a[i]].push_back(i);
			deg[a[i]]++;
	//		printf("[%d,%d] ", a[i], deg[a[i]]);
		}
		scanf("%s", st + 1);
		int m;
		scanf("%d", &m);
		for(int i(0); i < m; i++) {

			scanf("%s", tmp);
			cl[i] = string(tmp);
		}
		static vector<int> vec;
		vec.clear();
		for(int i(1); i <= n; i++) {
			if(deg[i] == 0) {
				vec.push_back(i);
			}
		}
		for(int i(0); i < (int)vec.size(); i++) {
			int v(vec[i]);
			deg[a[v]]--;
			if(deg[a[v]] == 0) {
				vec.push_back(a[v]);
			}
		}
		for(int i(0); i < m; i++) {
			cnt[i] = 0;
		}

		for(int _(0); _ < 10000; _++) {
			for(int i(0); i < (int)vec.size(); i++) {
				int v(vec[i]);
				s[vec[i]].clear();
				if(sons[vec[i]].empty()) {
					s[vec[i]].push_back(st[vec[i]]);
				}else {
					s[vec[i]].push_back(st[vec[i]]);
					static vector<int> rnd;
					rnd.clear();
					for(int j(0); j < (int)sons[vec[i]].size(); j++) {
						c[sons[v][j]] = 0;
						for(int k(0); k < (int)s[sons[v][j]].size(); k++) {
							rnd.push_back(sons[v][j]);
						}
					}
					random_shuffle(rnd.begin(), rnd.end());
					for(int j(0); j < (int)rnd.size(); j++) {
						s[v].push_back(s[rnd[j]][c[rnd[j]]++]);
					}
				}
			}
			//printf("%s\n", s[0].c_str());
			for(int i(0); i < m; i++) {
				if(s[0].find(cl[i]) != string::npos) {
					cnt[i]++;
				}
			}
		}
		//printf("%d %d\n", n, vec.size());
		printf("Case #%d:", qq);
		for(int i(0); i < m; i++) {
			printf(" %.10f", cnt[i]/10000.);
		}
		printf("\n");
	}
}
