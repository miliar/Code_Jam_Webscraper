#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(vector<ll> &count)
{
    for(int i = 0; i < 10; i++)
        if(count[i] == 0)   return false;
    return true;
}

ll solve(int N)
{
    if(N == 0)  return -1;
    vector<ll> count(10, 0);
    for(int i = 1; ; i++)
    {
        ll n = N * (ll)i;
        int d;
        while(n > 0)
        {
            d = n % 10;
            count[d]++;
            n = n / 10;
        }
        if(check(count))    return (N * i);
    }
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    freopen("A.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum)
    {
        int N;
        cin >> N;
        ll ans = solve(N);
        cout << "Case #" << tnum << ": ";
        if( ans == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << ans << endl;

    }
    return 0;
}
