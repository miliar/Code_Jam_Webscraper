#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

string S;
int Smax, bSum, Sum, num[1010];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        cin >> Smax;
        cin >> S;

        for (int i = 0; i <= Smax; ++i)
            num[i] = (int)S[i] - (int)'0';

        bSum = 0;
        for (int i = 0; i <= Smax; ++i)
            bSum += num[i];

        Sum = 0;
        for (int i = 0; i <= Smax; ++i)
            if (Sum >= i)
                Sum += num[i];
            else {
                Sum = i;
                Sum += num[i];
            }

        cout << Sum - bSum << endl;
    }
}
