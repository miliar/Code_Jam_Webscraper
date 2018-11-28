#include<iostream>
#include<string>
using namespace std;

int subs(string s, int n)
{
	int c=0;
	int cmax=0;
	for(int i=0;i<s.size();i++)
	{
		switch(s[i])
		{
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				{
					cmax=c>cmax?c:cmax;
					c=0;
					break;
				}
			default:
				{
					c++;
				}
		}
	}
	cmax=c>cmax?c:cmax;
	if(cmax>=n)
	{
		return 1;
	}
	else return 0;
}

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		cin>>s;
		int n;
		cin>>n;
		int count=0;
		for( int i=0;i<s.size();i++)
			for(int j=i+1;j<=s.size();j++)
			{
				count+=subs(s.substr(i,j-i),n);
			}
	cout<<"Case #"<<t<<": "<<count<<endl;
	
	}
	return 0;
}

