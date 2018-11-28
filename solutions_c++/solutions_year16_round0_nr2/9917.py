#include <iostream>
#include <cstring>
using namespace std;
int main()
{

	string s;
	int Test,n,i,j,ans=0;
	cin>>Test;
	for(j=1;j<=Test;j++)
	{
		ans=0;
		cin>>s;
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
			while(s[i]=='-' && i<s.length())
			{
				i++;
			}
			ans+=2;
			}

		}
		if(s[0]=='-')ans--;
		cout<<"Case #"<<j<<": "<<ans<<"\n";
	}
	return 0;
}