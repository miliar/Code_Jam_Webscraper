#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int flag=false,index,count=0,i=0;
		string s;
		cin>>s;
		if(s.length()==1&&s[0]=='-')
		{
			count=1;
			flag=true;
		}
		else if(s.length()==1&&s[0]=='+')
		{
			count=0;
			flag=true;
		}
		while(flag==false)
		{
			for(i=0;i<s.length()-1;i++)
			{
				if((s[i]=='+'&&s[i+1]=='-')||(s[i]=='-'&&s[i+1]=='+'))
				{
				index=i+1;
				count++;
				break;
				}
			}
				if((i==s.length()-1)&&(s[i]==s[i-1])&&s[i]=='-')
				{
				flag=true;
				count++;
				}
				else if((i==s.length()-1)&&(s[i]==s[i-1])&&s[i]=='+')
				flag=true;
				if(flag==false)
				{		
				for(int i=0;i<index;i++)
				if(s[i]=='-')
				s[i]='+';
				else
				s[i]='-';
				}
		}
			printf("Case #%d: %d\n",k,count);
	}
}
