#define ACTIVE
#ifdef ACTIVE
//#define SUBMIT

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

int main()
{
#ifdef SUBMIT
    freopen("/Users/nikitatarasov/Downloads/D-small-attempt0.in", "r", stdin);
    freopen("/Users/nikitatarasov/Downloads/D-small-attempt0.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int counter = 0; counter < t; ++counter)
    {
        int x, r, c;
        cin >> x >> r >> c;
        
        if(r < c)
            swap(r, c);
        
        if(x == 1)
            goto GABR;
        if(x == 2)
        {
            if((r == 3 && c == 3) || (r == 1 && c == 1) || (r == 3 && c == 1))
                goto RICH;
            else
                goto GABR;
        }
        if(x == 3)
        {
            if((r == 3 && c == 3) || (r == 3 && c == 2) || (r == 4 && c == 3))
                goto GABR;
            else
                goto RICH;
        }
        if((r == 4 && c == 3) || (r == 4 && c == 4))
            goto GABR;
        else
            goto RICH;
        
    GABR:
        cout << "Case #" << counter+1 << ": GABRIEL" << endl;
        continue;
    RICH:
        cout << "Case #" << counter+1 << ": RICHARD" << endl;
    }
    return 0;
}
#endif