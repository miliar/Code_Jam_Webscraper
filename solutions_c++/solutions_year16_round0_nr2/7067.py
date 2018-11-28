#include<iostream>
#include<fstream>
using namespace std;
int T;
string s;
int main()
{
	ifstream in("B-large.in");
	in>>T;
	for(int k=1;k<=T;k++)
	{
		in>>s;
		s+='+';
		int say=0;
		for(int i=0;i<s.length()-1;i++)
		{
			if(s[i]=='-' && s[i+1]=='+')
				say++;
		}
		cout<<"Case #"<<k<<": ";
		if(s[0]=='-')cout<<2*say-1<<endl;
		else cout<<2*say<<endl;
	}
}
