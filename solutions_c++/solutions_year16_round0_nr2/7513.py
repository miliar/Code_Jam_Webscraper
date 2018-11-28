#include <iostream>
#include <string>
using namespace std;

int pencake(string&,int,bool);

int main (void)
{
	int times;
	int length;
	cin>>times;
	string str;

	for(unsigned i=0; i<times; i++)
	{
		cin>>str;
		length=str.length();
		cout<<"Case #"<<(i+1)<<": "<<pencake(str,length,true)<<endl;

	}
	

}

int pencake(string &str, int len, bool check)
{
	if(check==true)
	{
		if(len==1)
		{
			if(str[0]=='+')
				return 0;
			else
				return 1;
		}
		else
		{
			if(str[len-1]=='+')
				return pencake(str,len-1,true);
			else
				return 1+pencake(str, len-1, false);
		}
	}
	else
	{
		if(len==1)
		{
			if(str[0]=='-')
				return 0;
			else
				return 1;
		}
		else
		{
			if(str[len-1]=='-')
				return pencake(str,len-1,false);
			else
				return 1+pencake(str, len-1, true);
		}
	}

}
