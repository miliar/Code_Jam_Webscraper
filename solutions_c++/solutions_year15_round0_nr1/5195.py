#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int main()
{
	int t;
	cin>>t;
		
	int tt;
	for(tt=1;tt<=t;tt++)
	{
		int l;
		cin>>l;
		
		string s;
		cin>>s;
		
		int ans = 0;
		int cCount = 0;
		int i;
		for(i=0;i<s.length();i++)
		{
			if(cCount >= i)
				cCount+=s[i]-'0';
			else
			{
				ans+=(i-cCount);
				cCount+=(i-cCount)+s[i]-'0';	
			}
			
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
		
	}
	
}