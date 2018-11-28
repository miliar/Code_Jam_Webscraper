#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF     INT_MAX
#define MAX     INT_MAX
#define MOD     1000000007
#define LL      long long


bool chk[11];

LL chkDigit(LL x)
{
    LL cnt = 0;
    while(x!=0)
    {
        if( !chk[x%10] )
        {
            chk[x%10] = true;
            cnt++;
        }

        x /= 10;
    }
    return cnt;
}

int main()
{
    READ();
    WRITE();

    int t;
    sf(t);
    int TC = 0;
    while(t--)
    {
        LL n;
        lsf(n);

        cout << "Case #" << ++TC << ": ";

        if(n == 0)
        {
            cout << "INSOMNIA" << endl;
        }
        else
        {
            memset(chk,false,sizeof(chk));
            LL chkCnt = 0;

            LL i = 1;

            while(chkCnt < 10)
            {
                chkCnt += chkDigit(n*i);
                i++;
            }
            cout << n*(i-1) << endl;
        }


    }


    return 0;
}
