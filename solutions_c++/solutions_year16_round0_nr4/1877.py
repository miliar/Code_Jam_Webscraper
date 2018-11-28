#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define RI(x) scanf("%d", &x)
#define RL(x) scanf("%I64d", &x)
#define RD(x) scanf("%f", &x)


void solve(int case_number)
{
    int s;
    cin >> s >> s >> s;
    cout << "Case #" << case_number << ": ";
    for (int i=1; i<=s; ++i)
        cout << i << ' ';
    cout << "\n";
}

int main()
{
    freopen("input4.in", "r", stdin);
    freopen("output4.out", "w", stdout);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)
        solve(i);

    return 0;
}

