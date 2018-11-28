#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
string s;
int k,res;
void solve()
{
	cin >> s >> k;
	res=0;
	for (int i=0; i+k-1<s.size(); i++)
	if (s[i]=='-')
	{
		for (int j=i; j<=i+k-1; j++)
			if (s[j]=='+') s[j]='-';
			else s[j]='+';
		res++;
	}
	for (int i=0; i<s.size(); i++)
		if (s[i]=='-')
		{
			cout << "IMPOSSIBLE";
			return;
		}
	cout << res;
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}