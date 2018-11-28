#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define MAXN 100010
#define eps 1e-5
#define pi acos(-1.0)
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,T,n;
    char a[2000];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        scanf("%s",a);
        int sum=0,ant=0,num;
        for(int i=0;i<=n;i++)
        {
            num=a[i]-'0';
            if(sum<i)
            {
                ant+=i-sum;
                sum=i+num;
            }
            else
                sum+=num;
        }
        printf("Case #%d: %d\n",t,ant);
    }
    return 0;
}
