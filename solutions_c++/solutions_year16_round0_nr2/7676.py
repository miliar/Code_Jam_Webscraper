#include<iostream>
#include<string>
#include<fstream>
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
		string s;
		//cin>>s;
		read>>s;
		int count=0;
		char prev=' ',cur=' ';
		prev=s[0];
		for(int i=1;i<s.length();i++)
		{
			cur=s[i];
			if(cur=='+' && prev=='+')
			{}
			else if(cur=='-' && prev=='-')
			{}
			else if(cur=='+' && prev=='-')
			{
				count++;
				prev='+';
			}
			else if(cur=='-' && prev=='+')
			{
				count++;
				prev='-';
			}
		}
		if(prev=='-')
			count++;
		//cout<<"Case #"<<iter<<": "<<count<<"\n";
		output<<"Case #"<<iter<<": "<<count<<"\n";
		iter++;
	}
	
	return 0;
}
