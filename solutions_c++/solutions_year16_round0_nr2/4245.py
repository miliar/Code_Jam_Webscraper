#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input2.txt","r",stdin);
	freopen("ans2.txt","w",stdout);
	long long int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		char s[200];
		cin>>s;
		long long int i,j,k,l,m,n,len;
		len=strlen(s);
		if(len==1)
		{
			if(s[0]=='-')
				cout<<"Case #"<<z<<": 1"<<endl;
			else
				cout<<"Case #"<<z<<": 0"<<endl;
		}
		else
		{
			long long int count=0;
			while(1)
			{
				if(s[0]=='+')
				{
					for(i=0;i<len-1;i++)
					{
						if(s[i]=='+' && s[i+1]=='-')
						{
							j=i;
							break;
						}
						j=i;
					}
					if(i==len-1 && s[i]=='+')
					{
						cout<<"Case #"<<z<<": "<<count<<endl;
						break;
					}
					else
					{
						for(i=0;i<=j;i++)
						s[i]='-';
						count++;
					}
				}
				else if(s[0]=='-')
				{
					for(i=0;i<len-1;i++)
					{
						if(s[i]=='-' && s[i+1]=='+')
						{
							j=i;
							break;
						}
						j=i;
					}
					if(i==len-1 && s[i]=='-')
					{
						j=i;
					}
					for(i=0;i<=j;i++)
					s[i]='+';
					count++;
				}
			}
		}
	}
	return 0;
}