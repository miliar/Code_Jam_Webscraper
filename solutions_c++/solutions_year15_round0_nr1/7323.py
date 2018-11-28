#include<iostream>
#include<fstream>
#include<string>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#include<math.h>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iomanip>
#define MAXN 1000000
#define MOD 10000000000
#define LL long long
#define eps 1e-8
#define inf 0x3f3f3f3f
using namespace std;

int main()
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    int Smax, levelnum;
    for(int ca = 1; ca <= T; ca++)
    {
        int sum = 0, extra = 0;
        scanf("%d", &Smax);
        for(int i = 0; i <= Smax; i++)
        {
            scanf("%1d", &levelnum);
            if(sum < i)
            {
                extra += i - sum;
                sum = i;
            }
            sum += levelnum;
        }
        printf("Case #%d: %d\n", ca, extra);
    }
    return 0;
}
