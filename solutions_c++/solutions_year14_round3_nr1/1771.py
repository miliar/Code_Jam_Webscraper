#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll P,Q;
int main(void)
{
	freopen("A-small-attempt1.in","rb",stdin);
	freopen("A-small-attempt1.out","wb",stdout);
	int T,t=1;
	scanf("%d",&T);

	while(t<=T)
	{
		scanf("%lld/%lld",&P,&Q);
		ll ans=0;
		if(Q%P==0){Q=Q/P;P=1;}
		//cout<<P<<" "<<Q<<endl;
		if((Q & Q-1)==0)
		{
			ll s=Q;
			while(s>P)
			{
				s>>=1;
				ans++;
			}
			printf("Case #%d: %lld\n",t,ans);
		}
		else printf("Case #%d: impossible\n",t);
		t++;
	}
	return 0;
}
