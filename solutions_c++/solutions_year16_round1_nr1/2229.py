#include <iostream>
#include <algorithm>
using namespace std;

string foo(string s, int n)
{
	if(n==1)
		return s.substr(0,1);
	string temp = foo(s, n-1);
	string a = s[n-1] + temp;
	string b = temp + s[n-1];
	if(a>b)
		return a;
	else
		return b;
}

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		cin>>s;
		s = foo(s, s.size());
		cout<<"Case #"<<t<<": "<<s<<endl;
	}
	return 0;
}
