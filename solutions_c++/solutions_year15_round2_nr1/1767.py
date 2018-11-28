#define _CRT_SECURE_NO_WARNINGS
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<vector>
#include<cctype>
#include<bitset>
#include<sstream>
#include<stdio.h>
#include<cstring>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<limits.h>
#define mp make_pair
using namespace std;
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int n, m;
bool vis[1111111];
int count(int n){
	if (n >= 10 && n < 100)
		return 1;
	if (n >= 100 && n < 1000)
		return 2;
	if (n >= 1000 && n < 10000)
		return 3;
	if (n >= 10000 && n < 100000)
		return 4;
	if (n >= 100000 && n < 1000000)
		return 5;
	if (n >= 1000000 && n < 10000000)
		return 6;
}
int bfs(int a){
	queue<int>q;
	q.push(a);
	int lev = 1;
	while (!q.empty()){
		int ss = q.size();
		while (ss--){
			int x = q.front();
			//cout << x << endl;
			q.pop();
			if (vis[x])continue;
			vis[x] = 1;
			if (x == n)
				return lev;
			if (x + 1 <= n)
				q.push(x + 1);
			int y = x;
			int c=0;
			int po = count(y);
			while (y > 0){
				int b = y % 10;
			    c += (b*pow(10, po));
				po--;
				y /= 10;
			}
			if (c <= n)
				q.push(c);
		}
		lev++;
	}
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
	int t,u=1;
	cin >> t;
	while (t--){
		memset(vis, 0, sizeof(vis));
		cin >> n;
		printf("Case #%d: ", u++);
		if (n < 12){
			cout << n << endl;
			continue;
		}
		else{
			long long c = 11;
			c+=bfs(12);
			cout << c << endl;
			continue;
		}
	}
	return 0;
}