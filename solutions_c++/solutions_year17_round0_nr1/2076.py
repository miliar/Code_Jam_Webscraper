#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

const int INF = (int)(1e9 + 1337);
const int64 LINF = (int64)(4e18);
const double EPS = (double)(1e-11);
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)

int n, k;
string s;

void solve()
{
    cin >> s >> k;
    n = s.size();
    int ctr = 0;
    for(int i = 0; i < n; i++)
    {
        if(s[i] == '-')
        {
            if(i + k > n)
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
            ctr++;
            for(int j = i; j < i + k; j++)
            {
                if(s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
        }
    }
    cout << ctr << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int ts;
    cin >> ts;
    for(int i = 1; i <= ts; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}

