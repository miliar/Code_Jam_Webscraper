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
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outcakelarge.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t, i, j, l, ans;
    string s;
    cin >> t;
    for(j = 1; j <= t; j++)
    {
        cin >> s;
        l = s.length();
        if(s[l-1] == '+')
            ans = 0;
        else
            ans = 1;
        for(i = l-2; i >= 0; i--)
        {
            if(s[i] != s[i+1])
                ans++;
        }
        cout << "Case #" << j << ": " << ans << '\n';
    }
	return 0;
}
