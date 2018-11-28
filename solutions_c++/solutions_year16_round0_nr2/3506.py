#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cout<<"Case #"<<j<<": ";
		string s;
		cin>>s;char ch=s[0];int count=0;
		for(int i=1;i<s.length();i++)
		{
			if(ch!=s[i])
			{
				count++;

			}
			ch=s[i];
		}
		if(s[0]=='-')
		{
			if(count%2==0)
				count++;
		}
		else
		{
			if(count%2!=0)
				count++;
		}
		cout<<count<<"\n";

	}
	return 0;
}