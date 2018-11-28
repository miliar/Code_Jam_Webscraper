#include <cstdio>
int teste;
int n,ct;
char ch;
int main()
{
    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);
    scanf("%d",&teste);
    for(int x=0;x<teste;x++)
    {
        scanf("%d",&n);
        scanf("%c",&ch);
        scanf("%c",&ch);
        int sum=ch-'0';
        //printf("%c ",ch);
        for(int i=1;i<=n;i++)
        {
            scanf("%c",&ch);
         //   printf("%c ",ch);
            int nr=ch-'0';
            if(nr!=0)
            {
                if(sum<i)
                {
                    ct+=i-sum;
                    sum=i;
                }
                sum+=nr;
            }
        }
       // printf("\n");
        printf("Case #%d: %d\n",x+1,ct);
        ct=0;
    }
}
