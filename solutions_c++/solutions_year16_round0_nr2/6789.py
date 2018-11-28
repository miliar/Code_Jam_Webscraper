#include<bits/stdc++.h>
#define sz 100001
using namespace std;
int main()
{
	int t,i,len,ans,b,k,f,g;
	string s;
//	freopen("1.txt","r",stdin);
//	freopen("2.txt","w",stdout);
	cin>>t;
	k=1;
	while(t--)
	{
		cin>>s;
		ans=0;
		len=s.length();
		if(len==1)
		{
			if(s[0]=='-')
				cout<<"Case #"<<k++<<": 1"<<endl;
			else
				cout<<"Case #"<<k++<<": 0"<<endl;
			continue;
		}
		i=0;
		if(s[i]=='+')
		{
			while(i<len && s[i++]=='+');
			if(i==len && s[i-1]!='-')
			{
				cout<<"Case #"<<k++<<": 0"<<endl;
				continue;
			}
			else
			{
				ans++;
				i--;
			}
		}
		f=0;g=0;
		for(i;i<len;i++)
		{
			if(s[i]=='+')
			{
				if(f==0)
				ans++;
				f=1;
			}
			else
			{
				if(g==1)
				{
					if(f==1)
					ans++;
					f=0;
				}
				if(g==0)
				{
					g=1;
				}
			}
		}
		if(s[i-1]=='-')
			ans++;
		cout<<"Case #"<<k++<<": "<<ans<<endl;
	}
}

