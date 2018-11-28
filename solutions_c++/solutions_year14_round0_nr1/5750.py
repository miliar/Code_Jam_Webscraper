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
int t, n, s;
set<int>x, y;
set<int>::iterator it;
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k){
		x.clear();
		y.clear();
		printf("Case #%d: ", k);
		scanf("%d", &n);
		--n;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &s);
				if (i == n)
					x.insert(s);
			}
		}
		scanf("%d", &n);
		--n;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &s);
				if (i == n)
					y.insert(s);
			}
		}
		vector<int>v;
		for (it = x.begin(); it != x.end();++it)
		if (y.find(*it) != y.end())
			v.push_back(*it);
		if (v.size() == 1)
			printf("%d", v[0]);
		else if (!v.size())
			printf("Volunteer cheated!");
		else printf("Bad magician!");
		puts("");
	}
}