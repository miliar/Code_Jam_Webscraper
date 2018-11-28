/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 30;

int P[MAXN];

int main()
{
    freopen("inputA.in", "r", stdin);
    freopen("outputA.out", "w", stdout);

    int _T;
    cin >> _T;

    for (int _t = 1; _t <= _T; _t++)
    {
        cout << "Case #" << _t << ": ";
        int N;
        cin >> N;

        int Sum = 0;
        for (int i = 0; i < N; i++)
        {
            cin >> P[i];
            Sum += P[i];
        }

        while(Sum > 0)
        {
            int maxCount = 1;
            int maxVal = P[0];

            for (int i = 1; i < N; i++)
            {
                if (P[i] > maxVal)
                {
                    maxVal = P[i];
                    maxCount = 1;
                }
                else if (P[i] == maxVal)
                {
                    maxCount++;
                }
            }

            assert(2 * maxVal <= Sum);
            int toDelete = (maxCount == 2 ? 2 : 1);
            Sum -= toDelete;

            for (int i = 0; toDelete > 0; i++)
            {
                if (maxVal == P[i])
                {
                    cout << char('A' + i);
                    P[i]--;
                    toDelete--;
                }
            }
            cout << " ";
        }
        cout << endl;
    }

    return 0;
}
