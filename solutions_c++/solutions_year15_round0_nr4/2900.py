/* Written By Manav Aggarwal */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int main()
{	
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("Ominous-Omino-Output.out", "w", stdout);
	ll t, cases;
	cin >> t;
	cases = t;
	while(t--)
	{
		ll x, r, c;
		string winner;
		cin >> x >> r >> c;
		if(x == 1)
		{
			winner = "GABRIEL";
		}
		else if(x == 2)
		{
			if((r*c) % x == 0)
			{
				winner = "GABRIEL";
			}
			else
			{
				winner = "RICHARD";
			}
		}
		else if(x == 3)
		{
			if((r*c) % x != 0)
			{
				winner = "RICHARD";
			}
			else
			{
				if(r == 1 || c == 1)
				{
					winner = "RICHARD";
				}
				else
				{
					winner = "GABRIEL";
				}
			}
		}
		else if(x == 4)
		{
			if((r*c) % x != 0)
			{
				winner = "RICHARD";
			}
			else
			{
				if(r <= 2 || c <= 2)
				{
					winner = "RICHARD";
				}
				else
				{
					winner = "GABRIEL";
				}
			}
		}
		cout << "Case #" << (cases - t) << ": " << winner << endl;
	}
	return 0;
}
