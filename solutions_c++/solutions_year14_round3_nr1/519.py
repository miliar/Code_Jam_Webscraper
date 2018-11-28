#include <iostream>
#include <vector>
#include <set>
#include <cstdio>
#include <algorithm>
#include <map>

#define sz(A) (int(A.size()))
#define int64 long long

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    int64 denum = (1LL << 40LL);

    for (int t = 0; t < T; t++)
    {
        int64 a, b;
        char c;
        cin >> a >> c >> b;
        cout << "Case #" << t + 1 << ": ";

        if (a * denum % b != 0)
            cout << "impossible\n";
        else
        {
            int64 num = a * denum / b;
            int res = 0;

            while (num > 0)
            {
                num /= 2;
                res++;
            }
            cout << 41 - res << '\n';
        }
    }

    return 0;
}
