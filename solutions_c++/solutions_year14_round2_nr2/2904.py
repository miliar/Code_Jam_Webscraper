#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.in","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int a,b,c,res=0;
        scanf("%d%d%d",&a,&b,&c);
        for(int j=0;j<a;j++)
        {
            for(int k=0;k<b;k++)
            {
                int n=j&k;
                //printf("%d\n",n);
                if(n<c)
                {

                    res++;
                }
            }
            //printf("%d\n",res);
        }
        printf("Case #%d: %d\n",i,res);
    }
    return 0;
}
