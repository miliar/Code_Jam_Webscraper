#include <iostream>
#include <vector>
#include <set>
#include <cstdio>
#include <algorithm>

#define sz(A) (int(A.size()))

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int a, b, k;
        cin >> a >> b >> k;
        int res = 0;

        for (int i = 0; i < a; i++)
            for (int j = 0; j < b; j++)
                if ((i & j) < k)
                    res++;
        cout << "Case #" << t + 1 << ": " << res << '\n';
    }
    return 0;
}
