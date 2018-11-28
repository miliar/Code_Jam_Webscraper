#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <math.h>
#include <iostream>

using namespace std;


int T, N;

char s[200000];
char ss[2000];
vector<string> str[30];

set<string> en[2], ch;

int res;



void dfs(int v, int ans)
{
	if (v == N) {
		res = min(ans, res);
		return ;
	}

	vector<int> check, check_2;
	int ini = 0;


	for (int w = 0; w < 2; w++) {
		ini = 0;
		for (int i = 0; i < int(str[v].size()); i++) {
			if (en[w].find(str[v][i]) == en[w].end())
				check.push_back(1);
			else
				check.push_back(0);
			en[w].insert(str[v][i]);

			if (en[(w+1)%2].find(str[v][i]) != en[(w+1)%2].end()) {
				if (ch.find(str[v][i]) == ch.end()) {
					ch.insert(str[v][i]);
					check_2.push_back(1);
					ini++;
				}else {
					check_2.push_back(0);
				}
			}else {
				check_2.push_back(0);
			}
		}

		dfs(v+1, ans+ini);
		for (int i = 0; i < int(check.size()); i++) {
			if (check[i] == 1)
				en[w].erase(str[v][i]);
			if (check_2[i] == 1)
				ch.erase(str[v][i]);
		}

		check.clear();
		check_2.clear();
	}
}


void solve()
{	
	en[0].clear();
	en[1].clear();
	ch.clear();

	int ans = 0;

	for (int i = 0; i < int(str[0].size()); i++)
		en[0].insert(str[0][i]);
	for (int i = 0; i < int(str[1].size()); i++) {
		if (en[0].find(str[1][i]) != en[0].end()) {
			ans++;
			ch.insert(str[1][i]);
		}

		en[1].insert(str[1][i]);
	}

	dfs(2, ans);
}


int main()
{
	scanf(" %d", &T);

	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d",&N);
		res = 0;
		gets(s);
		for (int i = 0; i < N; i++) {
			gets(s);

			int len = strlen(s);
			sscanf(s, " %s", ss);
			str[i].clear();
			str[i].push_back(string(ss));
			for (int j = 0; j < len; j++) {
				if (s[j] == ' ') {
					sscanf(&s[j], " %s", ss);
					str[i].push_back(string(ss));
					res++;
				}
			}
		}

		solve();
		fprintf(stderr, "case %d\n",cas);
		printf("Case #%d: %d\n", cas, res);
	}

	return 0;
}