//Problem C
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<cstring>
#include<string>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) revv(x,a,b,1)
#define mp make_pair
#define pb push_back
#define INF 2000000000
#define ll long long
using namespace std;

char l[10005]={};
int d[10005]={};
int e[4][4]={};
int t,n,m,p,a;

int num(int k,int l){
	int b=(k&4)^(l&4);
	return e[k&3][l&3]^b;
}

int main(){
	e[0][0]=0;e[0][1]=1;e[0][2]=2;e[0][3]=3;
	e[1][0]=1;e[1][1]=4;e[1][2]=3;e[1][3]=6;
	e[2][0]=2;e[2][1]=7;e[2][2]=4;e[2][3]=1;
	e[3][0]=3;e[3][1]=2;e[3][2]=5;e[3][3]=4;
	scanf("%d",&t);
	repp(x,1,t){
		scanf("%d %d",&n,&m);
		scanf("%s",l);
		p=n*m;
		a=0;
		repp(y,0,p-1){
			d[y]=l[y%n]-'i'+1;
			if(d[y-1]!=a)d[y]=num(d[y-1],d[y]);
			else a++;
			if(a==3)a=8;
		}
		if(d[p-1]==3&&a==8)printf("Case #%d: YES\n",x);
		else printf("Case #%d: NO\n",x);
	}
	return 0;
}
