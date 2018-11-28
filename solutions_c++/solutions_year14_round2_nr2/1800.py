#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,tt;
    scanf(" %d",&t);
    for(tt=1;tt<=t;tt++)
    {
        int a,b,k,i,j;
        scanf(" %d %d %d",&a,&b,&k);
        int res = 0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j) < k)
                {
                    //printf(" %d %d %d\n",i,j,i&j);
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",tt,res);
    }
    return 0;
}
