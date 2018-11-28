#include <stdio.h>
#include <string.h>

int num[10001]={0};

bool check(int n)
{
    int s[5],max=0;
    while(n)
    {
        s[max++]=n%10;
        n/=10;
    }
    for(int i=0;i<max/2;++i)
        if(s[i]!=s[max-1-i])
            return false;
    return true;
}

void set()
{
    for(int i=1;i<=100;++i)
        num[i*i]=i;
    for(int i=1;i<1001;++i)
        if(num[i]!=0&&check(num[i])&&check(i))
            num[i]=1;
        else
            num[i]=0;
}

int main()
{
    set();
    int t,n,m,c=0;
    scanf("%d",&t);
    while(t--)
    {
        c++;
        scanf("%d %d",&n,&m);
        printf("Case #%d: ",c);
        int sum=0;
        for(int i=n;i<=m;++i)
            sum+=num[i];
            printf("%d\n",sum);
    }
    return 0;
}
