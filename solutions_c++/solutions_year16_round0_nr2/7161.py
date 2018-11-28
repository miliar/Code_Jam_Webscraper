#include <bits/stdc++.h>
using namespace std;
int T,l;
string s;
int main()
{
	//ifstream cin("B-large.in");
	//ofstream cout("B.out");
	cin>>T;
	for(int c=1; c<=T; c++)
	{
		cin>>s;
		l=s.length();
		int cnt=1;
		for(int i=1; i<l; i++)
		if(s[i]!=s[i-1])cnt++;
		if(s[l-1]=='+')cnt--;
		cout<<"Case #"<<c<<": "<<cnt<<endl;
	}
	return 0;
}
