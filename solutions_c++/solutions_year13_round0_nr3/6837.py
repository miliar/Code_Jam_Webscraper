#include<stdio.h>
#include<string.h>
#define num 1002
int pingfan[num];
int sum[num];
int huiwen[num];
int a[10],len;
int check_hw(int x)
{
    int i,j;
    i=0;
    while(x!=0)
    {
        a[i]=x%10;
        x=x/10;
        i++;
    }
    len=i;
    for(i=len-1; i>=0; i--)
        if(a[i]!=a[len-1-i])
            return 0;
    return 1;
}
int check(int x)
{
    int i,j;
    if(pingfan[x]==0)
        return 0;
    if(check_hw(x)==0)
        return 0;
    if(check_hw(pingfan[x])==0)
        return 0;
    return 1;
}
void init()
{
    int i,j;
    for(i=0; i<num; i++)
        if(check_hw(i))
            huiwen[i]=1;
    for(i=0; i*i<num; i++)
    {
        pingfan[i*i]=i;
    }
    sum[1]=2;
    for(i=2; i<num; i++)
    {
        if(check(i))
        {
            //printf("%d\n",i);
            sum[i]=sum[i-1]+1;
        }
        else
            sum[i]=sum[i-1];
    }
}
int main()
{
    init();
    freopen("out.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int cas,count=1,i,j;
    int begin,end;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d%d",&begin,&end);
        printf("Case #%d: ",count++);
        if(check(begin))
            printf("%d\n",sum[end]-sum[begin]+1);
        else
            printf("%d\n",sum[end]-sum[begin]);
    }
}
