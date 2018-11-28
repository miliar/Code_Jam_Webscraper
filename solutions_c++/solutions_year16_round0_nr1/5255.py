

#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <assert.h>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
LL dp[40];
using namespace std;
int main(int argc, const char * argv[]) {

    int t;
    S(t);
    for(int i = 1 ; i <= t ; i++)
    {
        LL n;
        Sl(n);
        if(n == 0)
        {    printf("Case #%d: INSOMNIA\n",i);
        }
        else if (n == 1)
        {    printf("Case #%d: 10\n",i);
        }
        else
        {
            LL k = 1;
            int count = 0;
            int arr[12];
            for(int i = 0 ; i < 12 ; i++)
            {   arr[i] = 0;
            }
            while (count != 10)
            {
                LL temp = n*k;
                while(temp != 0)
                {
                    LL value = temp%10;
                    if (arr[value] == 0) {
                        count += 1;
                        arr[value] = 1;
                    }
                    temp = temp/10;
                }
                k++;
            }
            printf("Case #%d: %lld\n",i,n*(k-1));
        }
    }
    return 0;
}
