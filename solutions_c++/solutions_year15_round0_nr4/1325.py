#include<stdio.h>
int check(int x,int a,int b)
{
    if(x>=7)
        return 0;
    if((a*b)%x!=0)
        return 0;
    if(x<=2)
        return 1;
    if(x==3)
        if(b>=2)
            return 1;
        else 
            return 0;
    if(x==4)
        if(b>=3)
            return 1;
        else 
            return 0;
    if(x==5)
        if(b>=3)
            return 1;
        else
            return 0;
    if(x==6)
        if(b>=4)
            return 1;
        else
            return 0;
}
int main()
{
    int task,maxtask,x,a,b,flag;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&maxtask);
    for(task=1;task<=maxtask;task++)
    {
        scanf("%d %d %d",&x,&a,&b);
        if(a<b)
        {
            a=a+b;
            b=a-b;
            a=a-b;
        }
        flag=check(x,a,b);
        if (flag)
            printf("Case #%d: GABRIEL\n",task);
        else
            printf("Case #%d: RICHARD\n",task);
    }    
    fclose(stdout);
}
