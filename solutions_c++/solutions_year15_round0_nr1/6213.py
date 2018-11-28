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
    int tc, t, n;
    char s[1005];

    scanf("%d",&t);

    for(tc = 1; tc <= t; ++tc)
    {
        scanf("%d",&n);
        ++n;
        scanf("%s",s);

        int sum = 0, ans = 0;
        for(int i=0; i<n; ++i)
        {
            if(i>sum)
            {
                ans += (i-sum);
                sum = i;
            }
            sum += (s[i]-'0');
            //printf("sum - %d ans - %d\n",sum,ans);
        }

        printf("Case #%d: %d\n", tc, ans);
    }

    return 0;
}
