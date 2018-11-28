#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define RI(x) scanf("%d", &x)
#define RL(x) scanf("%I64d", &x)
#define RD(x) scanf("%f", &x)

string s;

void solve(int case_number)
{
    cin >> s;
    int last = -1, new_last;
    for (int i=0; i<s.length(); ++i)
        if (s[i] == '-')
            last = i;
    int ans=0;
    for (ans=0; last > -1; ++ans)
    {
        new_last = -1;
        for (int i=0; i<=last; ++i)
        {
            if (s[i] == '-')
                s[i] = '+';
            else
            {
                s[i] = '-';
                new_last = i;
            }
        }
        last = new_last;
    }
    cout << "Case #" << case_number << ": " << ans << "\n";
}

int main()
{
    freopen("input2.in", "r", stdin);
    freopen("output2.out", "w", stdout);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)
        solve(i);

    return 0;
}

