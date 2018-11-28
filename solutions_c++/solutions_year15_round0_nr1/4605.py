#include<iostream>
using namespace std;
int main()
{
	long long int t,x=1;
	freopen("A-large.in","r",stdin);
freopen("largeout.in","w",stdout);
	cin>>t;
	while(t--)
	{
		long long int smax,sum=0,i,ans=0;
		cin>>smax;
		char s[smax+1];
		cin>>s;
		sum = sum + s[0]-48;
		for(i=1;i<smax+1;i++)
		{
		
			if(i>sum)
			{
			ans = ans + 1;
			sum = sum  + 1;
		}
		//cout<<ans<<" "<<sum<<endl;
		sum = s[i]-48+sum;
		//cout<<sum<<endl;
		}
		cout<<"Case"<<" "<<"#"<<x<<":"<<" "<<ans<<endl;
		x++;
	}
}
