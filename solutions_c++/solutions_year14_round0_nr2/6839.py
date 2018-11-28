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

long test, t;
double c, f, x, res, now, t1, t2;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> test;
    for (t = 1; t <= test; t++)
    {
        cin >> c >> f >> x;
        res = 0;
        now = 2;
        do
        {
            t1 = x/now;
            t2 = x/(now + f) + c/now;
            if (t1 > t2)
            {
               res = res + c/now;
               now = now + f;
            }
            else
            {
                res = res + x/now;
                break;
            }
        }
        while (1);
        printf("Case #%d: %.7lf\n",t,res);    
    }
    return 0;
}
