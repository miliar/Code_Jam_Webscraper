#include<iostream>
#include<cstdio>
#include <fstream>
using namespace std;

int main()
{
	freopen("g1.in","r",stdin);
	
	freopen("testo.out","w",stdout);
	
	int t,tc=1;
	scanf("%d",&t);
	while(tc<=t)
	{
		int smax,ans=0,nos=0,n,d;
		char str[1005];
		scanf("%d%s",&smax,str);
		
		for(int i=0;i<=smax;i++)
		{
			n=str[i]-'0';
			
			if(nos>=i)
			{
				nos+=n; 
			}
			else
			{
				d = i-nos;
				ans += d;
				nos += d+n;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
		tc++;
	}
	return 0;
}
