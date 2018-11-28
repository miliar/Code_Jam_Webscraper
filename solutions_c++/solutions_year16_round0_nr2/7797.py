#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int test=1;
	while(test<=t)
	{
		string str;
		cin>>str;
		int ik,cnt=0,i,flag=0;
		for (ik = 0; ik < str.length(); ++ik)
		{
			if (str[ik]!='-')
			{
				break;
			}
		}
		if (ik==str.length())
		{
			cout<<"Case #"<<test<<": "<<1<<endl;
		}
		else
		{
			for (i = 1; i < str.length(); ++i)
			{
				if (str[i-1]=='-'&&str[i]=='+')
				{
					cnt++;
					flag=1;
					break;
				}
				else if(str[i-1]=='+'&&str[i]=='-')
					break;
			}
			int j;
			if (flag==1)
			{
				for (j = i+1; j < str.length(); ++j)
				{
					if (str[j-1]=='+'&&str[j]=='-')
					{
						cnt=cnt+2;
					}
				}
			}
			else
			{
				for (j = 1; j < str.length(); ++j)
				{
					if (str[j-1]=='+'&&str[j]=='-')
					{
						cnt=cnt+2;
					}
				}
			}
			
			cout<<"Case #"<<test<<": "<<cnt<<endl;
		}
		test++;
	}
	return 0;
}