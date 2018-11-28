#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <ctime>
#include <stdint.h>

using namespace std;

struct CNode{
	int son[26];
	int ns;
};

CNode node[1000000];
int num = 0;
int ans = 0;
int nans = 0;
int n, m;
char s[10][12];
int len[10];
int tree[4];
int flag[11];

void dfs(int k)
{
	if(k >= m){
		for(int i = 0; i<n; ++i){
			if(flag[i] == 0)
				return;
		}
		if(ans < num){
			ans = num;
			nans = 1;
		}else if(ans == num){
			nans++;
		}
		return;
	}
	queue<int> q1, q2;
	for(int i = 0; i<n; ++i){
		int ff = flag[i];
		flag[i] = 1;
		int now = tree[i];
		for(int j = 0; j<len[k]; ++j){
			if(node[now].son[s[k][j]] == 0){
				node[now].son[s[k][j]] = num;
				num++;
				q1.push(now);
				q2.push(s[k][j]);
			}
			now = node[now].son[s[k][j]];
		}
		dfs(k+1);
		while(!q1.empty()){
			node[q1.front()].son[q2.front()] = 0;
			num--;
			q1.pop();
			q2.pop();
		}
		flag[i] = ff;
	}
}

void Solve()
{
	scanf("%d%d", &m, &n);
	for(int i = 0; i<m; ++i){
		scanf("%s", s[i]);
		len[i] = strlen(s[i]);
		for(int j = 0; j<len[i]; ++j){
			s[i][j] = s[i][j]-'A';
		}
	}
	ans = 0;
	memset(node, 0, sizeof(node));
	memset(flag, 0, sizeof(flag));
	for(int i = 0; i<n; ++i){
		tree[i] = i;
	}
	num = n;
	dfs(0);
	printf("%d %d\n", ans, nans);
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}

