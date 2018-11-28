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

    int t, T, i, j, n, k, moves;
    string str;

    cin >> T;

    //a string like -----+++---++++---+ is equivalent to -+-+-+

    for (t = 1; t <= T; t++)
    {
        cin >> str;

        moves = 0;

        for (i = str.size() - 1; i >= 0; i--)
        {
            if (str[i] == '-')
            {
                //we always need the first to have minus so it becomes plus on reversal
                if (i >= 1 && str[0] == '+')
                {
                    for (j = 0; j < i && str[j] == '+'; j++)
                    {
                        str[j] = '-';
                    }
                    moves++;
                }

                //reverse till ith item
                reverse(str.begin(), str.begin() + i + 1);

                //reverse each item
                for (j = 0; j <= i; j++)
                {
                    if (str[j] == '+')
                    {
                        str[j] = '-';
                    }
                    else
                    {
                        str[j] = '+';
                    }
                }

                moves++;

                //cout << i << " " << str << "\n";
            }
        }

        cout << "Case #" << t << ": " << moves << "\n";
    }

    return 0;
}
