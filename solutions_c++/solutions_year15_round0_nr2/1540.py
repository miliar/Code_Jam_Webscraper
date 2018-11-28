//Problem B
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
#define INF 200000000
#define ll long long
using namespace std;

int d[1005]={};
int t,n,a,p,r;

int main(){
	scanf("%d",&t);
	repp(x,1,t){
		a=0;
		r=INF;
		scanf("%d",&n);
		repp(y,1,n){
			scanf("%d",&d[y]);
			a=max(a,d[y]);
		}
		repp(y,1,a){
			p=0;
			repp(z,1,n)if(d[z]>y)p+=(d[z]-1)/y;
			r=min(r,p+y);
		}
		printf("Case #%d: %d\n",x,r);
	}
	return 0;
}
