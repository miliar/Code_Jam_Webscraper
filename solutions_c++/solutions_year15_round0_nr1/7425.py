#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int x; string s;
		cin>>x; cin>>s;
		//cout<<endl<<x<<s<<endl;
		long long int cnt=0,total=0;
		for(int i=0;i<x+1;i++)
		{
			if(i==0)
			{
				if((s[i]-'0')>0)
				{
					total=s[i]-'0';
				}
				else
				{
					total=1;
					cnt+=1;
				}
			}
			else
			{
				if(total==i)
				{
					if( (s[i]-'0')==0)
					{
					total+=1;
					cnt+=1;
					}
					else
					total+=(s[i]-'0');
				}	
				else if(total>i )//&& (s[i]-'0')>0)
				{
					total+=(s[i]-'0');
				}
				
			}
			if(total>=x)
				break;
		}
		cout<<"Case #"<<p<<": "<<cnt<<endl;
	}
	return 0;
}									
					
