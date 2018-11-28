/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = -1;

int toDecimal(string s, int b)
{
    int N = s.size() - 1;
    int exp = 1;
    int res = 0;

    while(N >= 0)
    {
        if (s[N] == '1')
        {
            res += exp;
        }
        exp *= b;
        N--;
    }

    return res;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    for (int _t = 1; _t <= T; _t++)
    {
        int N, J;
        cin >> N >> J;
        cout << "Case #" << _t << ":" << endl;

        for (int i = 0; i < J; i++)
        {
            int x = i;
            string s = "1";
            for (int r = 0; r < 6; r++)
            {
                s = char((x % 2) + '0') + s;
                x /= 2;

            }
            s = "1" + s;

            cout << s << s << " ";
            for (int i = 2; i <= 10; i++)
            {
                cout << toDecimal(s, i) << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
