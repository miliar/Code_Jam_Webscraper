#include <cstdio>
#include <iostream>
#include <iomanip>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <memory.h>
#include <ctime>
#include <cmath>

#define forn(i, n) for(int i = 0; i < int(n); ++i)

using namespace std;

bool can(vector<int> a, int r)
{
    int n = a.size();

    bool ok = true;
    forn(i, n)
        if (a[i] > r)
            ok = false;

    if (ok)
        return true;

    for (int j = 1; j < r; j++)
    {
        int sum = j;
        forn(i, n)
            if (a[i] > j)
            {
                for (int d = 1;; d++)
                {
                    int up = (a[i] + d) / (d + 1);
                    if (up <= j)
                    {
                        sum += d;
                        break;
                    }
                }
            }
        if (sum <= r)
            return true;
    }
    
    return false;
}

int main()
{
    int t;
    cin >> t;
    forn(tt, t)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        forn(i, n)
            cin >> a[i];
        int l = 1;
        int r = 1000000;
        while (r - l > 1)
        {
            int mid = (l + r) / 2;
            if (can(a, mid))
                r = mid;
            else
                l = mid;
        }
        for (int i = l; i <= r; i++)
            if (can(a, i))
            {
                cout << "Case #" << (tt + 1) << ": " << i << endl;
                break;
            }
    }
    return 0;
}
