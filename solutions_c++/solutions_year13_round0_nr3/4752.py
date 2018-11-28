#include <stdio.h>

int ans[10];
int check(int a)
{
    int num[30],p=0;
    while(a>0)
    {
        num[p++]=a%10;
        a/=10;
    }
    for(int j=0; j<p/2; j++)
    {
        if(num[j]!=num[p-1-j])
        return 0;
    }
    return 1;
}
int main()
{
    int p,q=0,k;
    for(int i=1; i<=40; i++)
    {
        if(check(i)&&check(i*i))
        {
            ans[q++]=i*i;
        }
    }
    int T,l,r,c=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&l,&r);
        int count=0;
        for(int i=0; i<q; i++)
        {
            if(ans[i]>r)break;
            if(ans[i]>=l)
            {
                count++;
            }
        }
        printf("Case #%d: %d\n",++c,count);
    }
    return 0;
}
