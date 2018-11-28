#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <string>
using namespace std;
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.txt");
	int t;
	cin>>t;
	string s;
	string a="";
	vector<char> v;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		cout<<"Case #"<<i<<": ";
		a=s[0];
		for(int j=1;j<s.size();j++)
	{
		if((a+s[j])< (s[j]+a)) a=s[j]+a; else a+=s[j];
	}
		cout<<a<<endl;
		v.clear();
	}
return 0;
}