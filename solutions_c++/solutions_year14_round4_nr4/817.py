#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
int mx, cnt;
vector<string> v[4];
vector<string> s;
int n, m;
vector<vector<int> > nodes;
int head;
void insert(string &s){
	int cur = head;
	for (int i = 0; i < s.size(); ++i){
		if (nodes[cur][s[i] - 'A'] == -1){
			nodes[cur][s[i] - 'A'] = nodes.size();
			nodes.push_back(vector<int>(26, -1));
		}
		cur = nodes[cur][s[i] - 'A'];
	}
}
int calc(vector<string> &v){
	nodes.clear();
	nodes.push_back(vector<int>(26,-1));
	int res = 0;
	for (int i = 0; i < v.size(); ++i)
		insert(v[i]);
	return nodes.size();
}
void calc(int i){
	if (i == m){
		for (int j = 0; j < n; ++j)
			if (!v[j].size())
				return;
		int res = 0;
		for (int j = 0; j < n; ++j)
			res += calc(v[j]);
		if (mx < res){
			mx = res;
			cnt = 0;
		}
		if (mx == res)
			++cnt;
		return;
	}
	for (int j = 0; j < n; ++j){
		v[j].push_back(s[i]);
		calc(i + 1);
		v[j].pop_back();
	}
}
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T){
		printf("Case #%d: ", T);
		scanf("%d%d", &m, &n);
		s.resize(m);
		for (int i = 0; i < m; ++i)
			cin >> s[i];
		mx = -1;
		cnt = 0;
		calc(0);
		printf("%d %d\n", mx, cnt);
	}
	return 0;
}