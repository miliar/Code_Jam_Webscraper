#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

bool a[20];
long test, t, i, j, x, row, col, dem, res;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin >> test;
    for (t = 1; t <= test; t++)
    {
        memset(a, false, sizeof(a));
        cin >> row;
        for (i = 1; i <= 4; i++)
        {
            for (j = 1; j <= 4; j++)
            {
                cin >> x;
                if (i == row) a[x] = true;
            }
        }
        dem = 0;
        cin >> col;
        for (i = 1; i <= 4; i++)
        {
            for (j = 1; j <= 4; j++)
            {
                cin >> x;
                if (i == col)
                {
                      if (a[x] == true)
                      {
                               res = x;
                               dem += 1;
                      }
                }
            }
        }
        cout << "Case #" << t << ": ";
        if (dem == 1) cout << res;
        if (dem == 0) cout << "Volunteer cheated!";
        if (dem > 1) cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
