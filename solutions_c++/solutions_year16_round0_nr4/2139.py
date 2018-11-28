#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define ll long long
using namespace std;

int T,k,c,s;

int main(){
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
	scanf("%d",&T);
	fo(i,1,T) {
		scanf("%d%d%d",&k,&c,&s);
		int ma=k / c;
		if (k % c) ma++;
		if (ma>s) {
			printf("Case #%d: IMPOSSIBLE\n",i);
			continue;
		}
		printf("Case #%d:",i);
		ll tot=ma*c;
		fo(i,1,ma) {
			ll ans=0;
			fo(j,1,c) {
				ll w;
				if (tot>k) w=k;
				else w=tot;
				if (j>1) w--;
				ans+=w*(ll)pow(k,j-1);
				tot--;
			}
			printf(" %lld",ans);
		}
		puts("");
	}
	return 0;
}
