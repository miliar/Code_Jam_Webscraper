#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	string *s;
	cin>>t;
	int ctr=1;
	s=new string[t];
	for(int i=0;i<t;i++)
	{
		cin>>s[i];
		int flag=0;
		for(int j=0;j<s[i].size();j++)
		{
			if(s[i][j]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			cout<<"Case #"<<i+1<<": 0"<<endl;
			continue;
		}
		if(s[i][s[i].size()-1]=='-')
		{
			ctr=1;
			for(int j=0;j<s[i].size()-1;j++)
			{
				if(s[i][j]!=s[i][j+1])
				{
					ctr++;
				}			
			}
			
			cout<<"Case #"<<i+1<<": "<<ctr<<endl;
			continue;
		}
		flag=0;
		int j=s[i].size()-1;
		while(s[i][j]=='+')
		{
			j--;
		}
		ctr=1;
		for(;j>0;j--)
		{
			
			
			if(s[i][j]!=s[i][j-1] && j>0)
			{
				ctr++;
			}			
			
						
		}
		cout<<"Case #"<<i+1<<": "<<ctr<<endl;
	}
	return 0;
}
