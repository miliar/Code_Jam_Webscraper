#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>
#include <algorithm>
///#define LL long long
#define LL __int64
#define abs(x) ((x)>0?(x):-(x))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define max3(a, b, c) (a>b?max(a, c):max(b, c))
#define min3(a, b, c) (a<b?min(a, c):min(b, c))
#define max4(a, b, c, d) max(max(a, b), max(c, d))
#define min4(a, b, c, d) min(min(a, b), min(c, d))
#define Ee 2.718281828459045
#define Pi acos(-1.0)
#define eps 1e-8
#define INF 1 << 30
using namespace std;
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,case1=1;
    scanf("%d",&t);
    double c,f,x,max1,cnt,div;
    while(t--)
    {
        cin>>c>>f>>x;
        max1=x/2;
        cnt=c/2;
        div=2+f;
        while(1)
        {
            if(max1>cnt+x/div)
            {
                max1=cnt+x/div;
                cnt+=c/div;
                div+=f;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n",case1++,max1);
    }
    return 0;
}
