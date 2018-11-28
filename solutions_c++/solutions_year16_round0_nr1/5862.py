#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
bool in[10];
int main()
{
	int T;
	ll n;
	freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		cin>>n;
		printf("Case #%d: ",t);
		if(n==0){puts("INSOMNIA");continue;}
		memset(in,0,sizeof(in));
		ll ans;
		int tot=0;
		for(int hh=1;;hh++){
			ll xx=n*hh;
			ll yy=xx;
			while(yy){
				int jj=yy%10;
				if(!in[jj])in[jj]=1,tot++;
				yy/=10;
			}
			if(tot==10){
				ans=xx;
				break;
			}
		}
		printf("%lld\n",ans);
	}
	return 0;
}

