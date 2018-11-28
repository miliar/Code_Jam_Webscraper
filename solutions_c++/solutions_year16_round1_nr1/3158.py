#include<iostream>
#include<string>
using namespace std;

int main()
{
	string s;
	int t;
	cin>>t;
	int count=1;
	while(t-->0)
	{
		cin>>s;
		string s1="";
		s1=s[0];
		for(int i=1;i<s.length();i++)
		{
			if(s[i]>=s1[0])
			{
				s1=s[i]+s1;
			}
			else
			{
				s1+=s[i];
			}

		}
		cout<<"Case #"<<count<<": "<<s1<<endl;
		count++;
	}
}