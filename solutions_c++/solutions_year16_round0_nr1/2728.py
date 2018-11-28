#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define ll long long
using namespace std;

int T,tot;

bool bz[15];

ll x;

int num;

void calc(ll now){
	while (now) {
		if (!bz[now % 10]) tot++;
		bz[now % 10]=1;
		now /= 10;
	}
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	while (T--) {
		num++;
		memset(bz,0,sizeof(bz));
		tot=0;
		scanf("%lld",&x);
		if (x==0) {
			printf("Case #%d: INSOMNIA\n",num);
			continue;
		}
		int ans=1;
		while (tot<10) {
			calc(ans*x);
			if (tot==10) {
				printf("Case #%d: %lld\n",num,ans*x);
				break;
			}
			ans++;
		}
		
	}
	return 0;
}
