#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;
bool palin(int a)
{
    int t1=a,t2=0;
    while(t1!=0)
    {
        t2=t2*10+t1%10;
        t1/=10;
    }
    return (a==t2);
}
int main()
{
    int t,a,b,c,count=0;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&a,&b);
        c=a+b;
        b=max(a,b);
        a=c-b;
        count=0;
        for(int j=a;j<=b;j++)
        {
            if(palin(j))
            {
                if(sqrt(j)-(int)sqrt(j)==0.0)
                {
                    if(palin((int)sqrt(j)))
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n",i,count);
    }
    return 0;

}
