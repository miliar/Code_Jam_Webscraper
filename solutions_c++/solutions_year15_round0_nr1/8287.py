#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int test,t,person,ans,n,i;
	string str;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		ans=0;
		person=0;
		cin>>n;
		cin>>str;
		person+=(str[0]-'0');
		for(i=1;i<=n;i++)
		{
			if(person<i)
			{
				ans+=i-person;
				person=i;
			}
			person+=(str[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
