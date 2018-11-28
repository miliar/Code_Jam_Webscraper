#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string s;
int n;
int c = 0;

int main()
{
	int t;
	cin>>t;
	for (int tt=1; tt<=t; tt++)
	{
		cout<<"Case #"<<tt<<": ";
		
		cin>>s;
		n=s.length();
		c = 1;
		
		int t = 0;
		
		t = (s[0]=='-');
		for (int i=1; i<n; i++)
			if (s[i]!=s[i-1]) c++;
		
		int r = 0;
		if (!t) c--,r++;
		if (c%2) r += c;
		else r += c-1;
		
		cout<<r;
		cout<<'\n';
	}
    return 0;
}

