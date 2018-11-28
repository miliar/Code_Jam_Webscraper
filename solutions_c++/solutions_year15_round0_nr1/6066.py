/* Written By Manav Aggarwal */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int main()
{	
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("Standing-Ovation-Output1.out", "w", stdout);
	ll t, cases;
	cin >> t;
	cases = t;
	while(t--)
	{
		ll numberStanding = 0, minReq = 0, maxShyness;
		cin >> maxShyness;
		string audience;
		cin >> audience;
		for(int i = 0; i < audience.length(); i++)
		{
			if(numberStanding >= i)
			{
				numberStanding += audience[i] - '0';	
			}
			else if(audience[i] - '0' > 0)
			{
				minReq += (i - numberStanding);
				numberStanding += audience[i] - '0' + (i - numberStanding);
			}
		}
		cout << "Case #" << (cases - t) << ": " << minReq << endl;
	}
	return 0;
}
