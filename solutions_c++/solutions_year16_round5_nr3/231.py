#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf (1<<30)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define pdp pair<double,pii>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 1001000
#define mod 1000000007

#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)

typedef long long ll;
using namespace std;

struct edge {
	int a, b;
	ll dist;
	edge(int a=0,int b=0,ll dist=0): a(a), b(b), dist(dist) {}
	bool operator<(edge comp)const{
		return dist < comp.dist;
	}
};

int pai[maxn];

int find(int a){
	return pai[a] = (a == pai[a]) ? a : find(pai[a]);
}

#define sq(x) ((ll)(x)*(x))
int x[maxn];
int y[maxn];
int z[maxn];

main(){

	int nt;
	scanf("%d",&nt);
	for(int t=1;t<=nt;t++){
		int n,s;
		scanf("%d%d",&n,&s);
		vector<edge> v;
		for(int i=0;i<n;i++)
			scanf("%d%d%d%*d%*d%*d",x+i,y+i,z+i);
		for(int i=0;i<n;i++)
			pai[i] = i;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++){
				ll d = sq(x[i]-x[j])+sq(y[i]-y[j])+sq(z[i]-z[j]);
				v.pb(edge(i,j,d));
			}
		sort(v.begin(),v.end());
		ll ans = 0;
		for(int i=0;i<v.size();i++){
			ans = v[i].dist;
			int A = find(v[i].a);
			int B = find(v[i].b);
			if(A == B)
				continue;
			pai[A] = B;
			if(find(0) == find(1))
				break;
		}
		printf("Case #%d: %.10lf\n",t,sqrt(ans));
	}
}
