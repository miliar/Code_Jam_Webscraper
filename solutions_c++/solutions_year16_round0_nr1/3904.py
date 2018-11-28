#include<stdio.h>
#include<conio.h>
int mark[100];
int main()
{
    int q;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&q);
    int k;
    for(k=1;k<=q;k++)
    {
        int a;
        scanf("%d",&a);
        int i=1,cnt=0,j;
        printf("Case #%d: ",k);
        if(a==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        while(cnt!=10)
        {
//            cout<<1;
            int x=a*i;
            i++;
            while(x)
            {
                if(mark[x%10]==0)
                {
                    mark[x%10]=1;
                    cnt++;
                }
                x/=10;
            }
        }
        i--;
        for(j=0;j<=9;j++)
            mark[j]=0;
        printf("%d\n",a*i);
    }
    return 0;
}
