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

bool isPowerOfTwo (int64_t x)
{
  return x && (!(x&(x-1)));
}

int main()
{
    int64_t t,p,q,ans;
    int fl;
    scanf("%lld",&t);
    for(int64_t ca=1;ca<=t;ca++)
    {
        fl=0;
        ans=0;
        scanf("%lld/%lld",&p,&q);
        if(!(isPowerOfTwo(q)))
        {
            printf("Case #%lld: impossible\n",ca);
            continue;
        }
        while(q>p)
        {
            q/=2;
            ans++;
        }
            printf("Case #%lld: %lld\n",ca,ans);
    }
    return 0;
}
