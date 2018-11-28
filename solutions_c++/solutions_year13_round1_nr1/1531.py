#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        long long r, t;
        cin >> r >> t;

        t -= 2 * r + 1;
        r += 2;
        int y = 1;
        while (t > 0)
        {
            if (t < 2 * r + 1)
                break;
            t -= 2 * r + 1;
            if (t >= 0)
                ++y;
            r += 2;
        }

        cout << "Case #"
             << i
             << ": "
             << y;
        cout << endl;
    }
    return 0;
}
