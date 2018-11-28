#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s,ans="";
		cin>>s;
		ans=s[0];int pointer=0;
		for(int j=1;j<s.length();j++)
		{
			if(s[j]>=s[pointer])
			{
				ans=s[j]+ans;
				pointer=j;
			}	
			else
			{
				ans=ans+s[j];
			}

		}
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
}