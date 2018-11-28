#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

#define LOCAL_EXEC 1


unsigned long long
PaintForNthRing (
    int N,
    unsigned long long R
    )
{
    unsigned long long A = 2 * (N - 1);
    return 2*R + 2*A + 1;
}


int
main ()
{
#if (LOCAL_EXEC == 1)
    freopen("D:\\Input.txt", "r", stdin);
    freopen("D:\\Output.txt", "w", stdout);
#endif

    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c)
    {
        unsigned long long R, T;
        cin >> R >> T;

        int Rings = 0;
        unsigned long long PaintUsed = 0;
        while (PaintUsed < T)
        {
            ++Rings;
            PaintUsed += PaintForNthRing(Rings, R);
        }

        if (PaintUsed > T)
        {
            --Rings;
        }

        cout << "Case #" << c << ": " << Rings << endl;
    }

    return 0;
}
