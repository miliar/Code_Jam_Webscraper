//GCJ - !C -  Prob A
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

int t,n;
pii maxx[5];
int dat[30];

int main(){
	scanf("%d",&t);
	repp(tc,1,t){
		repp(i,0,28)dat[i]=0;
		repp(i,0,3)maxx[i]=mp(0,' ');
		scanf("%d",&n);
		repp(i,1,n){
			scanf("%d",&dat[i]);
			maxx[1]=mp(dat[i],i);
			sort(maxx+1,maxx+1+3);
		}
		//
		printf("Case #%d:",tc);
		//
		while(maxx[3].ff!=maxx[2].ff){
			printf(" %c",'A'-1+maxx[3].ss);
			maxx[3].ff--;
			if(maxx[3].ff!=maxx[2].ff){
				printf("%c",'A'-1+maxx[3].ss);
				maxx[3].ff--;
			}
		}
		repp(i,1,n){
			if(i==maxx[3].ss||i==maxx[2].ss)continue;
			while(dat[i]-->0){
				printf(" %c",'A'-1+i);
				if(dat[i]-->0)printf("%c",'A'-1+i);
			}
		}
		n=maxx[3].ff;
		repp(i,1,n)printf(" %c%c",'A'-1+maxx[2].ss,'A'-1+maxx[3].ss);
		printf("\n");
	}
	return 0;
}
