#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string.h>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#define inf 1000*1000*1000
#define mod 1000000009
#define ff first
#define ss second
#define mp  make_pair
using namespace std;
long long te, ind, sm, ans, cur;
char s[1009];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%lld", &te);
    while(te--)
    {
        ind++;
        scanf("%lld", &sm);
        scanf("%s", &s);
        printf("Case #%lld: ", ind);
        ans=0, cur=0;
        for(int i=0;i<=sm;i++)
        {
            int x = s[i] - 48;
            if(x==0)
                continue;
            if(i <= cur)
            {
                cur += x;
                continue;
            }
            int z = i - cur;
            ans += z;
            cur += z;
            cur += x;
        }
        printf("%lld\n", ans);
    }
}
