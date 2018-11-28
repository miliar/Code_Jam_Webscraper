#include<iostream>
#include<string>
using namespace std;
int main()
{	
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<c<<": ";
		string f="";
		f=f+s[0];
		for(int i=1;i<(int)s.size();i++)
		{
			string t1=f+s[i];
			string t2=s[i]+f;
			if(t1.compare(t2) < 0)
			{
				f = t2;
			}
			else 
			{
				f = t1;
			}
		}
		cout<<f<<"\n";		
	}
	return 0;
}
