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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <stdint.h>

using namespace std;
#define LL_max 200000000000
#define mod 1000000007

#define LL long long
#define mp make_pair
#define pb push_back

int main()
{
    int t,ca=1;
    double c,f,x,tm,tmp,m,ck;
    scanf("%d",&t);
    while(t--)
    {
        tmp=tm=0;
        ck=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        m=(double)x/2.0;
        while(true)
        {
            tm+=(double)c/(double)ck;
            ck+=(double)f;
            tmp=(double)tm+((double)x/(double)ck);
            if(m>tmp)
                m=tmp;
            else if(tmp>m)
                break;
        }
        printf("Case #%d: ",ca);
        printf("%.7f\n",m);
        ca++;
    }
    return 0;
}
