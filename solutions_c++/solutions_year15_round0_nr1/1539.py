//Problem A
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

char c[1005]={};
int t,n,r,p,q;

int main(){
	scanf("%d",&t);
	repp(x,1,t){
		p=q=r=0;
		scanf("%d",&n);
		scanf("%s",c);
		repp(y,0,n){
			p=0;
			if(q<y)p=y-q;
			r+=p;
			q+=p+c[y]-'0';
		}
		printf("Case #%d: %d\n",x,r);
	}
	return 0;
}
