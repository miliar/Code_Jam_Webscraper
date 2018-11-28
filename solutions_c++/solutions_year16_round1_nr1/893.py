#include<iostream>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		string s;
		cin>>s;
		int n=s.length();
		string ans="";
		ans+=s[0];
		for(int i=1;i<n;i++)
		{
			if(s[i]>=ans[0])
			{
				ans=s[i]+ans;
			}
			else
			{
				ans=ans+s[i];
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
}
