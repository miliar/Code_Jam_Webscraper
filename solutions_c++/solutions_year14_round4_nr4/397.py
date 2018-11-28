#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>


using namespace std;

int T;
int cas;
int N,M;

string s[10];
vector<string> v[10];
int ans,cnt;


int ff(int l,int r,int c,int idx)
{
	if( l+1 == r )return v[idx][l].length()-c+1;
	int i = l;
	int cc = 0;
	for( int j = l; j < r; j++ ){
		if( v[idx][i].substr(0,c) != v[idx][j].substr(0,c) ){
			cc += ff(i,j,c+1,idx)+1;
			i = j;
		}
	}
	cc += ff(i,r,c+1,idx)+1;
	return cc;
}

int cheeck()
{
	int cc = 0;
	for( int i = 0; i < N; i++ ){
		if( int(v[i].size()) == 0 )return -1;
		//for( int j = 0; j )
		//printf("ddd\n");
		cc += ff(0,int(v[i].size()),1,i)+1;
	}
	return cc;
}

void dfs(int now)
{
	if( now == M ){
		int ch = cheeck();
		//printf("%d\n",ch);
		if( ch > ans ){
			ans = ch;
			cnt = 1;
		}else if( ch == ans ){
			cnt++;
		}
	}else{
		for( int i = 0; i < N; i++ ){
			v[i].push_back(s[now]);
			dfs(now+1);
			v[i].pop_back();
		}
	}
}

void solve()
{
	for( int i = 0; i < N; i++ )
		v[i].clear();
	ans = 0;
	cnt = 1;
	dfs(0);
	printf("Case #%d: %d %d\n",cas,ans,cnt);
}

int main()
{
	scanf(" %d",&T);

	for( cas = 1; cas <= T; cas++ ){
		scanf(" %d %d",&M,&N);
		for( int i = 0; i < M; i++ )
			cin >> s[i];
		sort(s,s+M);
		solve();
	}

	return 0;
}