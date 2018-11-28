#include <iostream>
using namespace std;
int solve(string s);
int main() 
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<aa+1<<": "<<solve(s)<<endl;
	}
}
int solve(string s)
{
	s+="+";
	int ret =0;
	for(int i=1; i<s.size(); i++)
	{
		ret+=s[i]!=s[i-1];
	}
	return ret;
}
