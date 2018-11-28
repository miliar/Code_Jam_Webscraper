#include<stdio.h>
typedef long long ll;
ll ans[55][11],c=0;
int main()
{
	freopen("c.out","w",stdout);
	int t=1,cas,n,j,b;
	ll i,k,r,d;
	for(cas=1;cas<=t;cas++)
	{
		n=16,j=50;
		for(i=(1ll<<(ll)(n-1))+1ll;i<(1ll<<(ll)n);i++)
		{
			if((i&1)==0)continue;
			for(b=2;b<=10;b++)
			{
				ll ii=i;
				r=0;
				k=1;
				while(ii)
				{
					
					if(ii&1ll)r+=k;
					k*=b;
					ii>>=1ll;
				}
				ans[c][0]=i;
				bool fl=false;
				for(d=2;d*d<=r;d++)
				{
					if(r%d==0 && d!=r)
					{
						fl=true;
						ans[c][b]=d;
						break;
					}
				}
				if(fl==false)
				{
					c--;
					break;
				}
			}
			c++;
			if(c==j)break;
		}
	}
	printf("Case #1:\n");
	for(i=0;i<c;i++)
	{
		char ch[40];
		int le=0;
		while(ans[i][0])
		{
			ch[le++]='0'+(ans[i][0]&1);
			ans[i][0]>>=1;
		}
		for(j=le-1;j>=0;j--)putchar(ch[j]);
		for(j=2;j<=10;j++)printf(" %I64d",ans[i][j]);
		puts("");
	}
	fclose(stdout);
	return 0;
}
