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
    int t, tc, r1, r2;
    int mp[20], cardNum, count, ans;

    scanf("%d",&t);

    for(tc = 1; tc <= t; ++tc)
    {
        SET(mp,0);
        count = 0;

        scanf("%d",&r1);
        for(int i = 1; i <= 4; ++i)
        {
            for(int j = 1; j <= 4; ++j)
            {
                scanf("%d",&cardNum);
                if(i == r1)
                    mp[cardNum] += 1;
            }
        }

        scanf("%d",&r2);
        for(int i = 1; i <= 4; ++i)
        {
            for(int j = 1; j <= 4; ++j)
            {
                scanf("%d",&cardNum);
                if(i == r2 && mp[cardNum])
                {
                    ans = cardNum;
                    ++count;
                }
            }
        }

        printf("Case #%d: ", tc);

        if(count == 0)
            printf("Volunteer cheated!\n");
        else if(count == 1)
            printf("%d\n",ans);
        else
            printf("Bad magician!\n");
    }

    return 0;
}
