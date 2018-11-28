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
    //freopen("D--large.in","r",stdin);
    //freopen("data.out","w",stdout);
    int t,case1=1,n;
    double numn[1005],numk[1005];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&numn[i]);
        }
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&numk[i]);
        }
        sort(numn,numn+n);
        sort(numk,numk+n);
        int p=0,q=2*n-1,j=0,cnt1=0,cnt2=n;
        while(j<n)
        {
            if(numn[cnt1]<numk[j])
            {
                cnt1++;
            }
            j++;
        }
        cnt1=n-cnt1;
        int i=n-1;
        j=n-1;
        while(j>=0)
        {
            if(numn[i]>numk[j])
            {
                i--;
                j--;
            }
            else
            {
                cnt2--;
                j--;
            }
        }
        printf("Case #%d: %d %d\n",case1++,cnt2,cnt1);
    }
    return 0;
}
