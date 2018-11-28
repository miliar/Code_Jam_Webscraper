#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#define X first
#define Y second
#define fo(i,n) for(int i=0;i<n;i++)
#define fr(i,n) for(int i=1;i<=n;i++)
#define pb push_back

using namespace std;

typedef long long ll;

const int mod=(int)1e9+7;
int cas,T;
double c,f,x;

int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%lf%lf%lf",&c,&f,&x);
		double limit=f*(x-c)/c;
		double st=2.0,ans=0.0;
		while(st<=limit){
			ans+=c/st;
			st+=f;
		}
		ans+=x/st;
		printf("Case #%d: %.9lf\n",++cas,ans);
	}
	return 0;
}

