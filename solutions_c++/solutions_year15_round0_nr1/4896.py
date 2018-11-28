#include<bits/stdc++.h>
using namespace std;
int main()
{
	int p;
	scanf("%d",&p);
	for(int t=1;t<=p;t++)
	{
		char str[1100];
		int n;
		scanf("%d",&n);
		//getchar();
		scanf("%s",str);
		//printf("%s\n",str);
		
		int ans=0,i,x=0;
		//ans=str[i]-'0';
		for(i=0;i<=n;i++)
		{
					
					if(ans>=i)
					{
						ans+=str[i]-'0';
						continue;
					}
					else
					{
						if(str[i]!='0'){
						x+=(i-ans);
					     ans+=(i-ans);
					                 }    
					}
					ans+=str[i]-'0';
		}
		printf("Case #%d: %d\n",t,x);
		
	}
	return 0;
}
