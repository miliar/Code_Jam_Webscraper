#include <bits/stdc++.h>
using namespace std;

int count(string s)
{
	int i=0,x=0;
	if(s.at(0)=='-')
		x=1;
	while(i<s.length() && s.at(i)=='-')
		i++;
	for(int j=i;j<s.length()-1;j++)
	{
		if(s.at(j)=='+' && s.at(j+1)=='-')
			x+=2;
	}
	return x;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int t;
	cin >> t;
	
	for(int i=1;i<=t;i++)
	{
		string s;
		cin >> s;
		int ans = count(s);
		cout << "Case #" << i << ": " << ans << endl;
	}
}
