#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
	ll k, c, s, i, j, t;
	cin >> t;
	for(i=0; i<t; i++)
	{
		cin >> k;
		cin >> c;
		cin >> s;
		if(k == s)
		{
			cout << "Case #"<< (i+1) <<": ";
			for(j=1; j<=k; j++)
			{
				cout << j << " ";
			}
			cout << '\n';
		}
	}
}