#include<bits/stdc++.h>

using namespace std;

string calc(string s)
{
	int size = s.size();
	string ans="";
	ans += s[0];
	for(int i=1;i<size;i++)
	{
		if(ans[0] <= s[i])
			ans = s[i] + ans;
		else
			ans = ans + s[i];
	}
	return ans;
}

int main()
{
	int t;
	string s;
	cin>>t;
	cin.get();
	for(int i=1;i<=t;i++)
	{
		getline(cin,s);
		cout<<"Case #"<<i<<": "<<calc(s)<<endl;
	}
	return 0;
}
