#include <iostream>
using namespace std;

int main()
{
	int t,start,end;
	char str[3000];
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		for(int j=0;j<3000;j++)
			str[j]='*';
		string s;
		cin>>s;
		int l=s.length();
		start=1500;
		end=1500;
		str[start]=s[0];
		for(int j=1;j<l;j++)
		{
			if(s[j]>=str[start])
			{
				start--;
				str[start]=s[j];
			}
			else
			{
				end++;
				str[end]=s[j];
			}
		}
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<3000;j++)
		{
			if(str[j]!='*')
				cout<<str[j];
		}
		cout<<endl;
	}
	return 0;
}
