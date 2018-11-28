#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
int n, m;
char s[1999];
vector<LL> vec, v;
set<LL> st;


void find(int x, int y){	
	if (y == x){
		FOR(i,0,x) s[i + x] = s[x - i - 1];
		s[x + x] = '\0';
		vec.PB(atol(s));
		st.insert(atol(s));
		FOR(i,1,x) s[i + x - 1] = s[x - i - 1];
		s[x + x - 1] = '\0';
		vec.PB(atol(s));
		st.insert(atol(s));
		return;
	}
	if (y){
		s[y] = '0';
		find(x, y + 1);
	}
	FOR(i,1,10){
		s[y] = '0' + i;
		find(x, y + 1);
	}
	return;
}

int ip(LL x){
	sprintf(s, "%lld", x);
	int l = strlen(s);
	FOR(i,0,l >> 1) if (s[i] != s[l - i - 1]) return 0;
	return 1;
}

int main(){
	int T;
	FOE(i,1,4) find(i,0);
	/*
	printf("%d\n", vec.size());
	int t = 0;
	FOR(i,1,100000000){
		if (ip(i)){
			if (!st.count(i)){
				puts("fail");
			}
			t++;
		}
	}
	printf("%d\n", t);
	*/
	FOR(i,0,vec.size()){
		LL tmp = vec[i] * vec[i];
		if (ip(tmp)) v.PB(tmp);
	}
	//FOR(i,0,v.size()) printf("%lld\n", v[i]);
	scanf("%d", &T);
	FOE(cc,1,T){
		LL a, b, ans = 0;
		scanf("%lld%lld", &a, &b);
		FOR(i,0,v.size()) if (a <= v[i] && v[i] <= b) ans++;
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}
