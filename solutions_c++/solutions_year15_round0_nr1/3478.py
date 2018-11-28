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

int main()
{
    int t;
    cin >> t;
    forn(tt, t)
    {
        int n;
        string s;
        cin >> n >> s;

        int stay = 0, ans = 0;
        forn(i, s.length())
        {
            int r = s[i] - '0';
            if (i > stay)
            {
                ans += i - stay;
                stay += i - stay;
            }
            stay += r;
        }

        cout << "Case #" << (tt + 1) << ": " << ans << endl;
    }

    return 0;
}
