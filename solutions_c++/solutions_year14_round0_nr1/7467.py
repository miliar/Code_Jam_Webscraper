#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int ans, ansA, ansB, A[101][101], B[101][101], use[101];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int Cas = 1; Cas <= T; ++Cas)
    {
        printf("Case %d: ", Cas);

        cin >> ansA;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                cin >> A[i][j];
        memset(use, false, sizeof(use));
        for (int j = 1; j <= 4; ++j)
            use[A[ansA][j]] = true;

        cin >> ansB;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                cin >> B[i][j];

        ans = 0;
        for (int j = 1; j <= 4; ++j)
            if (use[B[ansB][j]])
                ++ans;

        if (ans == 0)
            cout << "Volunteer cheated!" << endl;
        else
            if (ans > 1)
                cout << "Bad magician!" << endl;
            else
                for (int j = 1; j <= 4; ++j)
                    if (use[B[ansB][j]])
                        cout << B[ansB][j] << endl;
    }
    return 0;
}
