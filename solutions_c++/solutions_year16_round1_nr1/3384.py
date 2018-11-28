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
		string s2="";
		int len=s.length();
		//s2[0]=s[0];
		for(int j=0;j<len;j++)
		{
			if(s[j]<s2[0])
				s2=s2+s[j];
			else
				s2=s[j]+s2;
		}
		cout<<"Case #"<<i<<": "<<s2<<endl;
	}
}