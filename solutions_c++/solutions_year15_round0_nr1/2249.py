#include<stdio.h>
int main()
{
    int task,maxtask,i,total,s,num,maxs;
    char ch;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&maxtask);
    for(task=1;task<=maxtask;task++)
    {
        scanf("%d ",&maxs);
        total=0;
        s=0;
        num=0;
        for(i=0;i<=maxs;i++)
        {
            scanf("%c",&ch);
            num=ch-'0';
            if(s+total<i)
                total=i-s;
                    
            s+=num;
        }
        printf("Case #%d: %d\n",task,total);
    }
    fclose(stdout);
    return 0;
}
