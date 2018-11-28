#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	int T;
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>T;
	int i;
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		string s;
		cin>>s;
		int l=s.length();
		int f[300];
		int j;
		int k;
		for(j=0;j<l;j++)
		if(s[j]=='+')f[j]=1;
		else f[j]=0;
		int ans=0;
		for(j=l-1;j>=0;j--)
		{
			if(f[j]==1)continue ;
			else
			{
				for(k=0;k<=j;k++)
				{
					if(f[k]==0)f[k]=1;
					else f[k]=0;
				}
				ans++;
			}
		}
		cout<<ans<<endl;
		
	}
	return 0;
}
