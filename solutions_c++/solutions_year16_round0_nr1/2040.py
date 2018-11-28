//GCJ - Pre Elimination A
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

int t,n,data[15],res;

void check(int n){
	while(n){
		if(!data[n%10]){
			data[n%10]=1;
			data[10]++;
		}
		n/=10;
	}
}

int main(){
	scanf("%d",&t);
	repp(tc,1,t){
		scanf("%d",&n);
		res=1;
		repp(i,0,13)data[i]=0;
		repp(i,1,72){
			check(n*i);
			if(data[10]==10){
				printf("Case #%d: %d\n",tc,n*i);
				res=0;
				break;
			}
		}
		if(res)printf("Case #%d: INSOMNIA\n",tc);
		//
	}
	return 0;
}
