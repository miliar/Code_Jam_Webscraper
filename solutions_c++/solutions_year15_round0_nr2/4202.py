#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>

typedef long long ll;
typedef long double ld;

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;++a)
#define per(a,b,c) for(int a=b;a>=c;--a)
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define PII pair<int,int>
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

int p[1111];
int TT,n;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&TT);
	rep(T,1,TT){
		scanf("%d",&n);
		rep(i,1,n)	scanf("%d",&p[i]);
		int ans=1001;
		rep(lim,1,1000){
			int cur=lim;
			rep(i,1,n)	if	(p[i]>lim)	cur+=((p[i]+lim-1)/lim)-1;
			ans=min(ans,cur);
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return	0;
}
