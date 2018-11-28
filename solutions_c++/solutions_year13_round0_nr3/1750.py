/* @author Sidharth Gupta */

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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>

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

lli memo[50],sz;

int ispalin(lli n)
{
    int buff[30],i=0,j;

    while(n)
    {
        buff[i] = (int)(n%10);
        ++i;
        n/=10;
    }

    --i;
    for(j=0;j<i;++j,--i)
    {
        if(buff[i]!=buff[j])
            return 0;
    }
    return 1;
}

void precompute(lli n)
{
    lli i=1;
    sz = 0;
    for(i=1;i*i<=n;++i)
    {
        if(ispalin(i*i) && ispalin(i))
            memo[sz++] = i*i;
    }
}

int solve(lli n)
{
    int i;
    for(i=0;i<sz;++i)
    {
        if(memo[i]>n)
            break;
    }

    return i;
}

int main()
{
    int t,i,tc;
    lli a,b;

    precompute(100000000000000ll);

    scanf("%d",&tc);
    for(t = 1; t <= tc; ++t)
    {
        scanf("%lld%lld",&a,&b);
        printf("Case #%d: %d\n",t, solve(b)-solve(a-1));
    }

    return 0;
}

