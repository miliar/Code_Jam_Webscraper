#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
	int t,standing=0,invites=0,i,j,c,smax,iter=1,m;
	//cin>>t;
	string s;
	ifstream read("input.txt");
	ofstream output("output.txt");
	read>>t;
	while(t--)
	{
		standing=0;
		invites=0;
		m=0;
		//cin>>smax>>s;
		read>>smax>>s;
		for(i=0;i<s.length();i++)
		{
			c=s[i]-'0';
			if(c>0 && standing>=i)
			standing+=c;
			else
			{
				if(standing<i)
				{
					m=i-standing;
					standing+=c+m;
					invites+=m;
				}
			}
		}
		//cout<<"Case #"<<iter<<": "<<invites<<"\n";
		output<<"Case #"<<iter<<": "<<invites<<"\n";
		iter++;
	}
	return 0;
}
