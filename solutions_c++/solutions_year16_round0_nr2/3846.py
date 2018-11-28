#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		bool flag=false;
		int bit=0;
		int count=0;
		for(int j=s.length()-1;j>=0;j--)
		{
			if(s[j]=='-' && !flag)
				flag=true;
			if(flag)
			{
				int cbit=(s[j]=='-')?(-1):(1);
				if(bit!=cbit)
				{
					count++;
					bit=cbit;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
