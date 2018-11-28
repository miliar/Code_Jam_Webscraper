#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
//#define maxn 50001
#define maxq 50001
#define maxe 100001
#define inf 100000007
#define ll long long
template <class T> T f_max(T x,T y){return x>y?x:y;}
template <class T> T f_min(T x,T y){return x<y?x:y;}
template <class T> void f_swap(T &x,T &y){T t;t=x,x=y,y=t;}
#define maxn 5
int a[maxn][maxn];
int b[maxn][maxn];
int main(){
	int n;
	int t;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	double c,f,x;
	int i,j,cas;
	for(cas=1;cas<=t;cas++){
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2;
		double tim=0;
		double v=2;
		while(tim<ans){
			tim+=c/v;
			v+=f;
			ans=f_min(ans,tim+x/v);
		}
		printf("Case #%d: %.7lf\n",cas,ans);
	}
	return 0;
}