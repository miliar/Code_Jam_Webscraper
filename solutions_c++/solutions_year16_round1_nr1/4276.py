#include<iostream>
#include<string.h>
#include<fstream>
#include<map>
using namespace std;
int main()
{
	int t,iter=1;
	ifstream read("input.txt");
	ofstream output("output.txt");
	read>>t;
	//cin>>t;
	while(t--)
	{
		string s,m="";
		//cin>>s;
		read>>s;
		m=s[0];
		int k=m[0];
		for(int i=1;i<s.length();i++)
		{
			int l=s[i];
			if(l>=k)
			{
				k=l;
				m=s[i]+m;
			}
			else
				m=m+s[i];
		}
		output<<"Case #"<<iter<<": "<<m<<"\n";
		//cout<<"Case #"<<iter<<": "<<m<<"\n";
		iter++;
	}
	
	return 0;
}
