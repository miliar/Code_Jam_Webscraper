
#include<stdio.h>
int main()
{
    int a,b,c,k,i,j;
    int t;
    int cs;
    int res;
    freopen("b_s.txt","r",stdin);
    scanf("%d",&t);
    cs=1;
    freopen("b_out.txt","w",stdout);
    while(cs<=t)
    {
        scanf("%d %d %d",&a,&b,&k);
        res=0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                c=i&j;
                if(c<k)
                {
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",cs,res);
        cs++;

    }
}
