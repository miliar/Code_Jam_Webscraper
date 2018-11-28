#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define eps 1e-13
#define endl '\n'
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pcc pair<char, char>
#define mp make_pair
#define F first
#define S second
#define pb push_back
ll modx(ll Base, ll exponent)
{
	ll ans = 1;
	while(exponent)
	{
		if(exponent & 1)
			ans = (ans * Base);
		Base = (Base * Base);
		exponent = exponent >> 1;
	}
	return ans;
}
int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("outtilesmall-2.txt","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
    int t, j;
    ll k, s, c, m, y, i;
    cin >> t;
    for(j = 1; j <= t; j++)
    {
        cin >> k >> c >> s;
        cout << "Case #" << j << ": ";
        if(c == 1 && s == k)
        {
            for(i = 1; i < k; i++)
                cout << i << " ";
            cout << k << '\n';
        }
        else if(s > (k-1)/2 && c > 1)
        {
            m = 2*modx(k, c-1);
            for(i = 2, y = 0; i <= k-1; i += 2, y += m)
                cout << (y+i) << " ";
            if(k % 2 == 0)
                cout << (y+i) << '\n';
            else
                cout << (y+1) << '\n';
        }
        else
            cout << "IMPOSSIBLE\n";
    }
	return 0;
}
