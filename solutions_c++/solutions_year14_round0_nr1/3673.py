#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>

#define int64 long long
#define sz(A) (int((A).size()))

using namespace std;

void get(vector <int> & res, int row)
{
    vector <int> input(4);

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
            cin >> input[j];

        if (i == row - 1)
            res = input;
    }
}

int main()
{
#ifdef shaoling
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int x, y;
        vector <int> A, B;
        cin >> x;
        get(A, x);
        cin >> y;
        get(B, y);

        int res = -1;

        for (int i = 0; i < 4; i++)
        {
            bool flag = 0;

            for (int j = 0; j < 4; j++)
                flag |= B[j] == A[i];
            
            if (flag)
            {
                if (res == -1)
                    res = A[i];
                else
                    res = -2;
            }
        }
        cout << "Case #" << t + 1 << ": ";

        if (res == -1)
            cout << "Volunteer cheated!\n";
        else if (res == -2)
            cout << "Bad magician!\n";
        else
            cout << res << '\n';
    }
    return 0;
}