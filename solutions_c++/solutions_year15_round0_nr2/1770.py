#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

int P[1002];
int dp[1002][1002];

int calc(int pos, int cutLeft)
{
    if( pos < 0 )
    {
        return 0;
    }

    int &ret = dp[pos][cutLeft];
    if(ret != -1)
    {
        return ret;
    }
    ret = (1<<30);

    for(int cut = 0; cut <= cutLeft; ++cut)
    {
        int val = P[pos]/(cut+1) + (P[pos]%(cut+1)==0?0:1);
        if( val + cut > P[pos] )
        {
            break;
        }

        val = max( val, calc(pos-1,cutLeft-cut) );
        ret = min( ret, val );
    }
    return ret;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T = INPT_INT;

    for(int ca = 1; ca <= T; ++ca)
    {
        int D = INPT_INT, res = 0;
        memset(dp,-1,sizeof(dp));

        for(int i = 0; i < D; ++i)
        {
            P[i] = INPT_INT;
            res = max(res, P[i]);
        }

        for(int i = res; i > 0; --i)
        {
            res = min(res, calc(D-1,i)+i);
        }
        printf("Case #%d: %d\n",ca,res);
    }
	return 0;
}
