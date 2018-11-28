#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<sstream>
using namespace std;
typedef long long ll;
ll ABS(ll x){
	if (x<0)return -x;
	return x;
}
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))
int t, len[101], n;
char g[101][101];
vector<pair<int, int> >v[101];
set<int>e;
pair<int,int> Get(int ith, int jth){
	if (jth+1 >= v[ith].size()){
		jth = (int)v[ith].size() - 1;
		e.insert(ith);
	}
	return v[ith][jth];
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k){
		char l = -1;
		int cnt = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i){
			scanf("%s", g[i]);
			len[i] = strlen(g[i]);
			v[i].clear();
			l = g[i][0];
			cnt = 0;
			for (int j = 0; j < len[i]; ++j){
				if (g[i][j] == l)++cnt;
				else{
					v[i].push_back(make_pair(l - 'a', cnt));
					cnt = 1;
					l = g[i][j];
				}
			}
			v[i].push_back(make_pair(l - 'a', cnt));
		}
		bool sol = 1;
		int res = 0;
		e.clear();
		for (int com = 0;sol &&  com < 100; ++com){
			if (e.size() == n)
				break;
			set<int>s;
			vector<int>temp;
			for (int i = 0; sol && i < n; ++i){
				pair<int, int> p = Get(i, com);
				s.insert(p.first);
				temp.push_back(p.second);
				if (s.size()>1)
					sol = 0;
			}
			int mn = (1 << 30);
			for (int r = 1; r <= 100; ++r){
				int sum = 0;
				for (int i = 0; i < n; ++i)
					sum += abs(r - temp[i]);
				mn = min(mn, sum);
			}
			res += mn;
		}
		printf("Case #%d: ", k);
		if (!sol)
			puts("Fegla Won");
		else printf("%d\n", res);
	}
}