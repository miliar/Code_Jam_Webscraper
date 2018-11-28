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
bool d[10];
void dig(int n)
{
    while(n > 0)
    {
        d[n%10] = true;
        n /= 10;
    }
}
bool check()
{
    int i;
    bool ans = d[0];
    for(i = 1; i < 10; i++)
        ans = ans & d[i];
    return ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outsheeplarge.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
	int t, n, i, j;
	bool ans;
	cin >> t;
    for(j = 1; j <= t; j++)
    {
        cin >> n;
        if(n == 0)
        {
            cout << "Case #" << j << ": INSOMNIA\n";
            continue;
        }
        for(i = 0; i < 10; i++)
            d[i] = false;
        ans = false;
        for(i = n; ; i+=n)
        {
            dig(i);
            if(check())
            {
                ans = true;
                break;
            }
        }
        if(ans)
            cout << "Case #" << j << ": " << i << '\n';
        else
            cout << "Case #" << j << ": INSOMNIA\n";
    }
	return 0;
}
