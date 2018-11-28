#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 100005
#define db double
#include<cmath>
#define eps 1e-8
using namespace std;

int N,J;

char ch[50];

int pri[maxn];

int bz[maxn];

int c[50];

int p[20];

void pq(int w){
	db now=0;
	fo(i,1,N) 
		if (c[i]) now=now+pow(w,(i-1));
	p[w]=0;
	fo(i,1,pri[0]){
		if (fabs(now-pri[i])<eps) continue;
		if (fabs(floor(now/pri[i]+0.5)*pri[i]-now)<eps) {
			p[w]=pri[i];
			break;
		}
	}
}

bool check(){
	fo(i,2,10) {
		pq(i);
		if (p[i]==0) return 0;
	}
	fd(i,N,1) printf("%d",c[i]);
	fo(i,2,10) printf(" %d",p[i]);
	puts("");
	return 1;
}

void dfs(int w){
	if (J==0) return;
	if (w==0) {
		if (check()) J--;
		return;
	}
	if (w==1||w==N) {
		c[w]=1;
		dfs(w-1);
		if (J==0) return;
		return;
	}
	if (J==0) return;
	c[w]=0;
	dfs(w-1);
	if (J==0) return;
	c[w]=1;
	dfs(w-1);
	if (J==0) return;
}

int main(){
	freopen("3.out","w",stdout);
	N=16;
	J=50;
	fo(i,2,100000)
		if (!bz[i]) {
			pri[++pri[0]]=i;
			fo(j,2,100000/i) bz[i*j]=1;
		}
	puts("Case #1:");
	dfs(N);
	return 0;
}
