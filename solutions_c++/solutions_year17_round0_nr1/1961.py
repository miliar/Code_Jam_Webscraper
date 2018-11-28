#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O2")
#define eb emplace_back
#define pb push_back
#define pw(x) ((1LL)<<(x))
#define buli(x) (__builtin_popcountll(x))
typedef long long ll;
typedef double db;
inline void rd(long long &x){
	int sign=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sign=-1,x=0):(x=c-'0');
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sign;
}
inline void rd(double&x){scanf("%lf",&x);}
inline void rd(int &x){ll y=0;rd(y);x=y;}


const int inf=1e9;
const int md=1e9+7;
const int maxn=1e5+10;
const db eps=1e-6;
char s[maxn];
int  a[maxn];
int n,m,T,x,y,z,nk,nq,ans;
void task(){
	scanf("%s",s+1);rd(nk);
	n = strlen(s + 1);
	for (int i = 1; i <= n ;i ++)
		if(s[i] == '-') a[i] = 1;
		else a[i] = 0;
	ans = 0;
	for (int i = 1; i <= n - nk + 1; i++) {
		if (a[i] == 1) {
			for(int j = i; j <= i + nk -1; ++j) a[j] =1 ^ a[j];
			++ans;
		}
	}
	for(int i = 1; i <= n; ++i) if(a[i] != 0) ans = inf;
	if (ans == inf) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);	
	
}
int main(){
	#ifdef GJY
		freopen("t.in","r",stdin);
		freopen("t.out","w",stdout);
	#endif
	rd(T);
	for(int ti = 1; ti <= T; ++ti){
		printf("Case #%d: ",ti);
		task();
	
	}
}





