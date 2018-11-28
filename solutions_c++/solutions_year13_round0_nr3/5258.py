#include<stdio.h>
#include <math.h>
int b[10];
int hui(int a)
{
    int r,i,j,k;
    k=1;
    for(i=0;i<4;i++)
    {
        r=a%10;
        b[i]=r;
        a/=10;
        if(a==0)break;
    }
    for(j=0;j<i;j++,i--)
    {
        if(b[j]!=b[i])
        {
            k=0;break;
        }
    }
    if(k==0)return 0;
    else return 1;
}
int main()
{
    freopen("A0.in","r",stdin);
    freopen("A00.txt","w",stdout);
   int t,a,b,i,ans,k;
   scanf("%d",&t);
   k=1;
   while(t--)
   {
       scanf("%d%d",&a,&b);
       printf("Case #%d: ",k++);
       ans=0;
       for(i=a;i<=b;i++)
       {
           if(hui(i)==1)
           {
               int f;
               f=sqrt(i);
               if(f*f==i)
               {
                   if(hui(f)==1)
                    ans++;
               }
           }
       }
       printf("%d\n",ans);
   }
   return 0;
}
