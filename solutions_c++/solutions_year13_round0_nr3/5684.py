#include<stdio.h>
#include<math.h>
bool judge(int x)
{
    int tmp=x;
    int y=0;
    while(tmp)
    {
       y*=10;
       y+=tmp%10;
       tmp/=10;
    }
    if(x!=y)
    return false;
    double a=sqrt(x*1.0);
    if(a!=(int)(a))
    return false;
    int t=(int)a;
    int b=0;
    while(t)
    {
        b*=10;
        b+=t%10;
        t/=10;
    }
    if((int)a!=b)
    return false;
    return true;
}

int main()
{
   // freopen("in.txt","r",stdin);
   // freopen("ou.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ii=1;
    while(t--)
    {
        printf("Case #%d: ",ii++);
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;i++)
        {
            if(judge(i))
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}

