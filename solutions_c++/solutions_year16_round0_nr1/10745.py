#include<stdio.h>
int digi(int a[10],int num);
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,tc;
    while(scanf("%d",&t)!=EOF)
    {
        for(tc=1; tc<=t; tc++)
        {
            long int n,no;
            int j;
            scanf("%ld",&n);
            j=1;
            if(n==0)
            {
                    printf("Case #%d: INSOMNIA\n",tc);
            }

            else
            {
                int digit[10]= {0,0,0,0,0,0,0,0,0,0};
            while(digit[0]!=1 || digit[1]!=1 || digit[2]!=1 || digit[3]!=1 || digit[4]!=1 || digit[5]!=1 || digit[6]!=1 || digit[7]!=1 || digit[8]!=1 || digit[9]!=1 )
            {
                // printf("%d ",no);
                no=n*j;
                digi(digit,no);
                j++;
            }
            //for(int k=0;k<10;k++)
            //printf("%d ",digit[k]);


                printf("Case #%d: %d\n",tc,no);
            }

        }
    }
}
int digi(int a[10],int num)
{
    int r;
    while(num!=0)
    {
        r=num%10;
        num/=10;
        a[r]=1;
    }
    return *a;
}
