/*************************************************************************
Author: zjut_polym
Created Time:   2013/4/27 8:44:13
File Name: codejam.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
struct node{
	int x, y, k;
	node(){};
	node(int _x, int _y, int _k):x(_x), y(_y), k(_k){};
};

struct att{
	int ti, day, l, r, str, sd, md, dd;
	friend bool operator < (att a, att b){
		return a.day > b.day;
	}
	
}tmp[105], cnt[105];
const int mv = 1004;
int str[100000000];
void gao(int n){
	int ans = 0;
	priority_queue <att> Q;
	for(int i = 0; i < n; i++)
		Q.push(tmp[i]);
	for(int i = 0; !Q.empty(); i++){
		int size = 0;
		while(!Q.empty() && Q.top().day == i){
			att top = Q.top(), p; Q.pop();
			cnt[size++] = top; 
			p = top;
			p.ti--;
			p.day += p.dd;
			p.l += p.md;
			p.r += p.md;
			p.str += p.sd;
			if(p.ti){
				Q.push(p);
			}
			bool flag = true;
			for(int i = (top.l + mv) * 2; i <= (top.r + mv) * 2 && flag; i++){
				if(str[i] < top.str) flag = false;
			}
			if(!flag) ans++;
		}
		for(int i = 0; i < size; i++){
			for(int j = (cnt[i].l + mv) * 2; j <= (cnt[i].r + mv) * 2; j++){
				str[j] = max(str[j], cnt[i].str);
			}
		}
	}
	printf("%d\n", ans);
}
int main() {
	int cas, c = 1, x, y, n;
	scanf("%d", &cas);
	while(cas--){
		scanf("%d", &n);
		memset(str, 0, sizeof(str));
		for(int i = 0; i < n; i++){
			scanf("%d%d%d%d%d%d%d%d", &tmp[i].day, &tmp[i].ti, &tmp[i].l, &tmp[i].r, &tmp[i].str, 
					&tmp[i].dd, &tmp[i].md, &tmp[i].sd);
		}
		printf("Case #%d: ", c++);
		gao(n);

	}
    return 0;
}

