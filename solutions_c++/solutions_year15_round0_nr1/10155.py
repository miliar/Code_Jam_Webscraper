#include <iostream>
using namespace std;

int main() 
{
	long test, ans, s, sum, k;
	char str[1000];
	cin>>test;
	for(k=1; k<=test; ++k)
	{
		cin>>s>>str;
		sum=ans=0;
		for(long i=0; i<=s; ++i)
		{
			
			if(i-sum>0)
			{
				ans+=i-sum;
				sum=i;
			}
			sum+=(str[i]-'0');
		}
		cout<<"Case #"<<k<<": "<<ans<<"\n";
	}
	return 0;
}