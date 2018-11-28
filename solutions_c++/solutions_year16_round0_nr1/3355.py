#include<cstdio>
#include<iostream>
using namespace std;
bool hv[10];
int main()
{
	int n,x,c,t,ans;
	bool flag;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>n;
	
	for(int i=1;i<=n;++i)
	{
		cin>>x;
		c=1;
		for(int j=0;j<10;++j) hv[j]=0;
		while(1)
		{
			if(x==0) break;
			t=c*x;ans=t;
			while(t>0)
			{
				hv[t%10]=1;
				t/=10;
			}
			c++;
			
			flag=1;
			for(int j=0;j<10;++j) if(hv[j]==0) {flag=0;break;}
				if(flag==1) break;
		}
		if(x==0)
		printf("Case #%d: INSOMNIA\n",i);
		else printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
