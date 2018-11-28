#include<bits/stdc++.h>
using namespace std;
 
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int t,a,b,k,i,m=0,j,ans=0;
	cin>>t;
	while(t--)
	{
		cin>>a>>b>>k;
		m++;ans=0;
		
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					ans++;
					//cout<<i<<" "<<j<<"\n";
				}
			}
		}
		printf("Case #%d: %d\n",m,ans);
	}
	return 0;
}

		
