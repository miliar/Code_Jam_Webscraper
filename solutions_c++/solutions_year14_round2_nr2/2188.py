#include<iostream>
using namespace std;
int main()
{
	int t,a,p,b,k,i,j;
	long int ans;
	cin>>t;
	for(p=0;p<t;p++)
	{
		ans=0;
		cin>>a>>b>>k;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i & j)< k)
				{
					ans++;
				}
			}
		}
		cout<<"Case #"<<p+1<<": "<<ans<<"\n";
	}
	return 0;
}
