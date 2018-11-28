#include <bits/stdc++.h>
using namespace std;

int counter(string s)
{
	int i=0,X=0;
	if(s.at(0)=='-')
		X=1;
	while(i<s.length() && s.at(i)=='-')
		i += 1;
	for(int j=i;j<s.length()-1;j++)
	{
		if(s.at(j)=='+' && s.at(j+1)=='-')
			X+=2;
	}
	return X;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int test;
	cin >> test;
	
	for(int i=1;i<=test;i++)
	{
		string s;
		cin >> s;
		int ans = counter(s);
		cout << "Case #" << i << ": " << ans << endl;
	}
}
