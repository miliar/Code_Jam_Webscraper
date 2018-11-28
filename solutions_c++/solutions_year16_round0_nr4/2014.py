//GCJ - Pre Elimination D
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<cstring>
#include<string>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define OO (int)2e9
#define INF (ll)9e18
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
using namespace std;

int t,k,c,s,l;

ll angka(int num,int depth){
	if(depth<=0)return 1;
	ll pos=num-depth;
	if(pos>k-1)pos=k-1;
	repp(i,1,depth-1)pos*=k;
	return pos + angka(num,depth-1);
}

int main(){
	scanf("%d",&t);
	repp(tc,1,t){
		scanf("%d %d %d",&k,&c,&s);
		if(k>c*s)printf("Case #%d: IMPOSSIBLE\n",tc);
		else{
			printf("Case #%d:",tc);
			l=(k+c-1)/c;
			repp(i,1,l)printf(" %lld",angka(i*c,c));
			printf("\n");
		}
	}
	return 0;
}
