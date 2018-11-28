#include <iostream>
using namespace std;

int main() {
	int t,i=0;
	cin>>t;
	while(t--)
	{
		i++;
		string s;
		int ans=0,flag=1;
		cin>>s;
		for(int j=s.length()-1;j>=0;j--)
		{
			if(s[j]=='+' && flag==0)
			{
				if(j-1>=0)
				{
					if(s[j-1]=='-')
					{
						ans++;
					}
				}
				if(j==0)
				{
					ans++;
				}
			}
			if(s[j]=='-')
			{
				flag=0;
				if(j-1>=0)
				{
					if(s[j-1]=='+')
					{
						ans++;
					}
				}
				if(j==0)
				{
					ans++;
				}
				
			}
		}
		
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}