#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		int len=s.length();
		int counter=0;
		if(len!=1)
		{
			
			for(int j=0;j<len-1;j++)
			{
				if(s[j]!=s[j+1])
					counter++;
			}
		}
		if(s[len-1]=='-')
			counter++;
		cout<<"Case #"<<i<<": "<<counter<<endl;
	}
}
