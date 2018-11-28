#include<stdio.h>
#include<string.h>
int num[20];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cnt=0;
    while(t--)
    {

        memset(num,0,sizeof(num));
        for(int i=0;i<2;i++)
        {
           int a;
            scanf("%d",&a);
            int b;
            for(int j=0;j<4;j++)
                for(int k=0;k<4;k++)
                {
                    scanf("%d",&b);
                    if(j==a-1)
                        num[b]++;
                }
        }
        int flag=0;
        int z;
        for(int i=1;i<=16;i++)
        {
            //printf("i-->%d  %d\n",i,num[i]);
            if(num[i]==2)
                z=i,flag++;
        }
        printf("Case #%d: ",++cnt);
        if(flag==1)
            printf("%d\n",z);
        else if(flag==0)
            printf("Volunteer cheated!\n");
        else if(flag>1)
            printf("Bad magician!\n");
    }
    return 0;
}
