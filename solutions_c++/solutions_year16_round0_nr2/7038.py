#include<bits/stdc++.h>

using namespace std;
#define ll long long


int main()
{
	ll t,n;
	ifstream myfile ("input2l.in");
	ofstream outfile("ans2l.txt");
	myfile>>t;
	//cin>>t;
	string s;
	for(ll test=1;test<=t;test++)
	{
		myfile>>s;
		//cin>>s;
		ll i,ans=0;
		if(s[1]=='\0')
		{
			if(s[0]=='-')
				ans++;
		}
		else
		{
			for(i=0;s[i]!='\0';i++)
			{
				if((s[i]=='-'&&s[i+1]=='+')||(s[i]=='+'&&s[i+1]=='-'))
				{
					ans++;
				}
			}
			if(s[i-1]=='-')
				ans++;
		}


		outfile<<"Case #"<<test<<": "<<ans<<endl;
		//cout<<"Case #"<<test<<": "<<ans<<endl;

	}


	return 0;
}
