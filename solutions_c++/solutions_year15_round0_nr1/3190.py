#include<stdio.h>
#include<string.h>
char s[1007];
int main()
{

    int t,cas=1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        int a[1001];
        int i;
        memset(a,0,sizeof(a));
        memset(s,0,sizeof(s));

        int n,countt=0;
        scanf("%d",&n);
        scanf("%s",&s);
        int l=strlen(s);
        for(i=0;i<l;i++)
            a[i]=s[i]-48;
//        for(i=0;i<l;i++)
//            printf("%d ",a[i]);
        int sum=0;
        int k=0;
        for(i=0;i<l;i++)
            {
                while(sum<i)
                {
                 sum++;k++;
                }
                if(sum>=i)
                     {sum+=a[i];/*printf("s=%d\n",sum);*/}
                //printf("%d\n",sum);
            }
    printf("Case #%d: %d\n",cas++,k);
    }
    return 0;
}
