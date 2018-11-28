#include<bits/stdc++.h>

#define MOD 1000000007
#define MODSET(d) if ((d) >= MOD) d %= MOD;

using namespace std;

int main()
{
    #ifdef VSP4
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif // VSP4

    int t, T, i, j, n, k, curr;
    set<int> digits;

    cin >> T;

    for (t = 1; t <= T; t++)
    {
        cin >> n;
        //n = t;

        if (n == 0)
        {
            cout << "Case #" << t << ": " << "INSOMNIA" << "\n";
        }
        else
        {
            digits.clear();

            curr = n;
            i = 1;

            while (true)
            {
                k = curr;
                while (k)
                {
                    digits.insert(k % 10);
                    k /= 10;
                }

                if (digits.size() == 10)
                    break;

                curr += n;
                i++;
            }

            cout << "Case #" << t << ": " << curr << "\n";
        }
    }

    return 0;
}
