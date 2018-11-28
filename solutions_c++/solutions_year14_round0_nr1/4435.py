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
    int t,case1=1,num[4],x;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d",&n);
        for(int i=1; i<=4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%d",&x);
                if(i==n)
                {
                    num[j]=x;
                }
            }
        }
        scanf("%d",&m);
        int cnt=0,y=-1;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&x);
                if(i==m)
                {
                    for(int k=0;k<4;k++)
                    {
                        if(num[k]==x)
                        {
                            cnt++;
                            y=k;
                        }
                    }
                }
            }
        }
        printf("Case #%d: ",case1++);
        if(cnt==0)
        {
            puts("Volunteer cheated!");
        }
        else if(cnt>1)
        {
            puts("Bad magician!");
        }
        else printf("%d\n",num[y]);
    }
    return 0;
}
