#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<algorithm>
using namespace std;

typedef long long ll;

double PI = 2.0*acos(0);

int main()
{
    freopen("As.in","r", stdin);
    freopen("AsOut.out","w",stdout);

    int T, kas=1;
    ll r, cnt, st, t;

    for(scanf("%d",&T); kas<=T; kas++)
    {
        scanf("%lld%lld",&r,&t);
        cnt=0;

        while( t>0 && t>=((2*r)+1) )
        {
            cnt++;
            t -= ((2*r)+1);
            r += 2LL;
        }

        printf("Case #%d: %lld\n",kas,cnt);
    }

    return 0;
}
