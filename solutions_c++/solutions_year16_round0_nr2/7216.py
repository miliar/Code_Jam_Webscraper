#include <bits/stdc++.h>
using namespace std;

int steps(string s, int r, char curr)
{
	if(r==0)
	{
		return 0;
	}
	if(s[r-1] == curr)
	{
		return steps(s, r-1, curr);
	}
	else
	{
		if(curr == '+'){curr = '-';}
		else{curr = '+';}
		return 1 + steps(s, r-1, curr);
	}
}

int main()
{
	int t,i=0;
	string s;
	cin>>t;
	while(i++<t)
	{
		cout<<"Case #"<<i<<": ";
		char curr = '+';
		cin>>s;
		int n = s.length();
		cout<<steps(s,n,curr)<<endl;
	}
}