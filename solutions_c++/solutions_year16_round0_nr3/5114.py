#include<bits/stdc++.h>
#define int64 long long
#define sqr(x) (x)*(x)
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define rep(i,x,y) for(int i=(x);i<=(y);++i)
#define VI vector<int>
#define VI64 vector<int64>
#define VS vector<string>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VPII vector< PII >
#define SZ(x) ((int)(x).size())
using namespace std;
const double pi=acos(-1);
int  n,J;
int a[120];
void dfs(int dep){
	if(!J)return;
	if(dep>=n){
		rep(i,1,n)printf("%d",a[i]);
		rep(i,2,10)printf(" %d",i+1);
		puts("");
		J--;
		return;
	}
	a[dep]=0;
	a[dep+1]=0;
	dfs(dep+2);
	a[dep]=1;
	a[dep+1]=1;
	dfs(dep+2);
}
int main(){
	freopen("c.out","w",stdout);
	n=32;
	J=500;
	a[n]=1;
	a[1]=1;
	printf("Case #1:\n");
	dfs(2);
}

