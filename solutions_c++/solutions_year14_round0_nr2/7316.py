/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>


#define MOD 1000000007
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

int main()
{
    int t, tc;
    double c, f, x;
    double s;
    double ans;
    double left;

    scanf("%d",&tc);
    for(t = 1; t <= tc; ++t)
    {
        s = (double)2;
        ans = (double)0;

        scanf("%lf%lf%lf",&c,&f,&x);

        while(1)
        {
            if((x < c) || (x/s < x/(s+f) + c/s))
            {
                ans += x/s;
                break;
            }
            else
            {
                ans += c/s;
                s += f;
            }
        }

        printf("Case #%d: ", t);
        printf("%.7f\n",ans);
    }

    return 0;
}
