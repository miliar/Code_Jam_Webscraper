#include<bits/stdc++.h>
using namespace std;
int ans=0;
int main(void)
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,c=1;
	cin>>t;
	while(t--)
	{
		ans=0;
		cout<<"Case #"<<c++<<": ";
		string s;
		cin>>s;
		int flag=0;
		while(1)
		{
			if(s[0]=='-')
			{
				++ans;
				int ctr=0;
				while(s[ctr]=='-' && ctr<s.size())
				{
					s[ctr]='+';
					++ctr;
				}
			}
			else
			{
				int ctr=0;
				while(s[ctr]=='+' && ctr<s.size())
				{
					s[ctr]='-';
					++ctr;
				}
				if(ctr==s.size())
				{
					flag=1;
					break;
				}				
				++ans;
			}			
		}		
		cout<<ans<<endl;
	}
	return 0;
}
