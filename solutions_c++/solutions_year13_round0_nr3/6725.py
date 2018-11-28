
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int find(int x)
{
    if(x<10)
     return 1;
     if(x==0)
        return 0;
     int a[100],j=0,i;
     while(x>=10)
     {
         a[j++]=x%10;
         x=x/10;
     }
     a[j++]=x;
     for(i=0;i<=(j-1)/2;i++)
     {
         if(a[i]!=a[j-1-i])
            return 0;
     }
     return 1;

}
int ok(int x)
{
    int i;
    for(i=1;i<=sqrt(x)+1;i++)
        if(i*i==x)
            return i;
    return 0;

}
int main()
{
//    freopen("C0.in.txt","r",stdin);
//    freopen("2.txt","w",stdout);
    int t,a,b,i,nas=0;
    scanf("%d",&t);
    while(t--)
    {
       int cout=0;
        scanf("%d%d",&a,&b);
        for( i=a;i<=b;i++)
        {
            if(find(ok(i))&&ok(i)&&find(i))
            {
                 cout++;
            }

        }
        nas++;
        printf("Case #%d: %d\n",nas,cout);

    }
return 0;
}
