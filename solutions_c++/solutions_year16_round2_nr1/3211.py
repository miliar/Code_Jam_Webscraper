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
ll gcd(ll a, ll b)
{
	if(b == 0)
		return a;
	return gcd(b, a%b);
}
ll modx(ll Base,ll exponent)
{
	ll ans = 1;
	while(exponent)
	{
		if(exponent & 1)
			ans = (ans * Base)%mod;
		Base = (Base * Base)%mod;
		exponent = exponent >> 1;
	}
	return ans;
}
bool cmp()
{

}
int a[26], n[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-largeout.txt","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
    int t, l, i, j;
    string s;
    cin >> t;
    for(j = 1; j <= t; j++)
    {
        cin >> s;
        l = s.length();
        for(i = 0; i < 26; i++)
            a[i] = 0;
        for(i = 0; i < l; i++)
            a[(int)s[i]-65]++;

        n[0] = a[25];
        a[4] -= n[0];
        a[17] -= n[0];
        a[14] -= n[0];

        n[2] = a[22];
        a[14] -= n[2];
        a[19] -= n[2];

        n[4] = a[20];
        a[5] -= n[4];
        a[14] -= n[4];
        a[17] -= n[4];

        n[6] = a[23];
        a[18] -= n[6];
        a[8] -= n[6];

        n[8] = a[6];
        a[4] -= n[8];
        a[8] -= n[8];
        a[7] -= n[8];
        a[19] -= n[8];

        n[1] = a[14];

        n[3] = a[19];

        n[5] = a[5];
        a[8] -= n[5];

        n[7] = a[18];

        n[9] = a[8];

        cout << "Case #" << j << ": ";

        for(i = 0; i < 10; i++)
        {
            for(int k = 0; k < n[i]; k++)
                cout << i;
        }
        cout << '\n';
    }
	return 0;
}
