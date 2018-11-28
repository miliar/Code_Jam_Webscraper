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
#define LL long long
//#define LL __int64
#define abs(x) ((x)>0?(x):-(x))
#define Ee 2.718281828459045
#define Pi acos(-1.0)
#define eps 1e-10
#define INF 1 << 28
using namespace std;
int min(int a,int b)
{
    if(a>b)a=b;
    return a;
}
int max(int a,int b)
{
    if(a<b)a=b;
    return a;
}
int main()
{
   // freopen("B--small-attempt0.in","r",stdin);
   // freopen("data.out","w",stdout);

    int t,a,b,k,case1=1;
    unsigned long long cnt=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&a,&b,&k);
        cnt=0;
        //cnt+=(unsigned long long)(a*(k-1))+(unsigned long long)(b*(k-1));
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j)<k)
                {
                    //printf("%d %d %d\n",i,j,i&j);
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",case1++,cnt);
    }
    return 0;
}
