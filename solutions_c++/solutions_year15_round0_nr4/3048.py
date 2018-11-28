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
    int t, tc, x, r, c;

    scanf("%d",&tc);
    for(t=1; t<= tc; ++t)
    {
        scanf("%d%d%d", &x,&r,&c);
        if(x==1)
            printf("Case #%d: GABRIEL\n",t);
        else if(x==2)
        {
            if(EVEN(r*c))
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
        else if(x==3)
        {
            if(r==1 || c==1 || ((r*c)%3))
                printf("Case #%d: RICHARD\n",t);
            else
                printf("Case #%d: GABRIEL\n",t);
        }
        else if(x==4)
        {
            if((r==4 && c==4) || (r*c==12))
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
    }

    return 0;
}
