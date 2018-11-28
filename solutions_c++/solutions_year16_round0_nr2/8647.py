#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int j,t,i,count,val,x;
	string s;
	cin>>t;
	val=0;
	while(t--)
	{
		count=0;
		cin>>s;
		i=s.length();
		if(i>1)
		{
			for(j=i-1;j>=0;j--)
			{
				if(s[j]=='+')
				continue;
				else
				{
					count++;
					for(x=j;x>=0;x--)
					{
						if(s[x]=='+')
						s[x]='-';
						else
						s[x]='+';
					}
				}
			}
		}
		else
		{
			if(s[0]=='-')
			count=1;
			else
			count=0;
		}
		val++;
		cout<<"Case #"<<val<<": "<<count<<endl;
		count=0;
	}
	return 0;
}