#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int maxN = 100;
const int maxL = 50;
int n, l;
string G[maxN], B;

int main()
{
    int ct, t;
    cin >> ct;

    for (t = 1; t <= ct; t ++)
    {
        cin >> n >> l;
        for (int i = 0; i < n; i ++)
        {
            cin >> G[i];
        }
        cin >> B;

        bool impossible = false;
        for (int i = 0; i < n; i ++)
        {
            if (B == G[i])
            {
                impossible = true;
            }
        }

        if (impossible)
        {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
        else
        {
            if (l == 1)
            {
                cout << "Case #" << t << ": 0 0?" << endl;
            }
            else
            {
                cout << "Case #" << t << ": ";
                for (int j = 1; j < l; j ++)
                    cout << "?";
                cout << " ";
                for (int j = 1; j < l; j ++)
                    cout << (l - j) % 2;
                cout << "0?";

                for (int j = 1; j < l; j ++)
                    cout << j % 2;
                cout << endl;
            }
        }
    }
    return 0;
}
