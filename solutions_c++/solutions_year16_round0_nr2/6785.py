#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
#define mod 1000000007

using namespace std;

int t;
string s;

int main()
{
    //freopen(".in", "r", stdin);
    freopen("B.out", "w", stdout);
    //ios_base::sync_with_stdio(0);
    cin.tie();
    cin >> t;
    for (int l = 1; l <= t; l++) {
        cin >> s;
        int c = 0;
        for (int j = 0; j < s.length() - 1; j++)
            if (s[j] == '-' && s[j + 1] == '+') c++;
            else if (s[j] == '+' && s[j + 1] == '-') c++;
        if (s[s.length() - 1] == '-') c++;
        cout << "Case #" << l << ": " << c << endl;
    }

    return 0;
}
