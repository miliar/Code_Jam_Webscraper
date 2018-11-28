#include <set>
#include <map>
#include <queue>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <cctype>
#include <algorithm>
#include <time.h>
#define eps 1e-10
#define pi acos(-1.0)
#define inf 107374182
#define inf64 1152921504606846976
#define lc l,m,tr<<1
#define rc m + 1,r,tr<<1|1
#define zero(a) fabs(a)<eps
#define iabs(x)  ((x) > 0 ? (x) : -(x))
#define clear1(A, X, SIZE) memset(A, X, sizeof(A[0]) * (min(SIZE,sizeof(A))))
#define clearall(A, X) memset(A, X, sizeof(A))
#define memcopy1(A , X, SIZE) memcpy(A , X ,sizeof(X[0])*(SIZE))
#define memcopyall(A, X) memcpy(A , X ,sizeof(X))
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
using namespace std;


int main()
{
    //freopen("A-large.in","r",stdin);
   //freopen("A-large.out","w",stdout);
    int t,case1=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,sum=0,ans=0;
        char s[1005];
        scanf("%d%s",&n,s);
        for(int i=0;i<=n;i++)
        {
            if(sum<i)
            {
                ans+=i-sum;
                sum=i;
                //printf("###%d\n",i);
            }
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",case1++,ans);
    }
    return 0;
}
