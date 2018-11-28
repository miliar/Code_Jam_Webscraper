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

int final[105][105];

int check(int n, int m, int x, int y)
{
    int flag = 0, i;

    for(i=0;i<n;++i)
    {
        if(final[i][y] > final[x][y])
        {
            flag = 1;
            break;
        }
    }

    if(!flag)
        return 1;

    for(i=0;i<m;++i)
    {
        if(final[x][i] > final[x][y])
        {
            flag = 2;
            break;
        }
    }

    if(flag == 2)
        return 0;
    return 1;
}

int main()
{
    int t,n,m,i,j,tc,flag;

    scanf("%d",&tc);

    for(t=1;t<=tc;++t)
    {
        scanf("%d%d",&n,&m);

        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                scanf("%d",&final[i][j]);
            }
        }

        flag = 0;
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                if(check(n,m,i,j)==0)
                {
                    flag = 1;
                    break;
                }
            }
            if(flag)
                break;
        }

        printf("Case #%d: ", t);
        if(flag)
            printf("NO\n");
        else
            printf("YES\n");
    }

    return 0;
}

