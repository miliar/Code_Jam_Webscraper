#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for (int j = 1; j <= t; j++)
    {
        bool d[10] = {0};
        unsigned long long n;
        bool sol = false;
        cin >> n;

        for (int i = 1; i <= 10000; i++)
        {
            unsigned long long c = i * n;
            while (c != 0)
            {
                d[c%10] = true;
                c /= 10;
            }
            if (d[0] && d[1] && d[2] && d[3] && d[4] && d[5] && d[6] && d[7] && d[8] && d[9])
            {
                cout << "Case #" << j <<  ": " << i * n << endl;
                sol = true;
                break;
            }
        }
        if (!sol)
            cout << "Case #" << j <<  ": INSOMNIA" << endl;
    }
    return 0;
}
