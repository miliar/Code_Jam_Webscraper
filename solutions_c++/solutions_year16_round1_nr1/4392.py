#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int t,i,j,k,n;
	string s,s1="",s2="";
	ofstream out("A-large.txt");
	cin>>t;
	for(n=0;n<t;n++)
	{
		cin>>s;
		//s1[0]=s[0];
		for(i=0;i<s.length();i++)
		{
			if(s1[0]<=s[i])
			{
				s2+=s[i];
				s2+=s1;
				s1=s2;
				s2="";
			}
			else
			{
				s2+=s1;
				s2+=s[i];
				s1=s2;
				s2="";
			}
		
		
		}
		
	out<<"Case #"<<n+1<<": "<<s1<<"\n";
	s1="";
	}

}
