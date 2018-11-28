#include<stdio.h>
#include<stdlib.h>

main()
{
    int a,t;
    scanf("%d",&t);
    for(a=0;a<t;a++)
    {
        int n,i,num=0,ans=0;
        scanf("%d",&n);
        char audi[n+1];
        scanf("%s",audi);
        //printf("%s",audi);
        num+=audi[0]-'0';
        for(i=1;i<=n;i++)
        {
            //printf("%d %d\n",i,num);
            if(audi[i]-'0'!=0 && i>num)
            {
                //printf(":");
                while(i>num)
                {
                    ans++;
                    num++;
                }
            }
            num+=audi[i]-'0';
        }
        printf("Case #%d: ",a+1);
        if(n==0) printf("0\n");
        else printf("%d\n",ans);
    }
}
