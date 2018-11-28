#include<iostream>
#include<cstdio>
#include<vector>
#include<climits>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>

using namespace std;
int main()
{
	long long int t,k,maxm,d,i,j,a[1005],ans,x;
	cin>>t;
	k=1;
	while(t--)
	{
		maxm=0;
		cin>>d;
		for(i=0;i<d;i++)
		{
			cin>>a[i];
			if(a[i]>maxm)
			maxm=a[i];
		}
		ans=INT_MAX;
		for(i=1;i<=maxm;i++)
		{
			x=0;
			for(j=0;j<d;j++)
			{
				x=x+(a[j]+i-1)/i-1;
			}
			x=x+i;
			ans=min(ans,x);
			
			
		}
		
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
	
	
    return 0;
}


