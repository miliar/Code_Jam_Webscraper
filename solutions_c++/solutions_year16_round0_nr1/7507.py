#include<stdio.h>

using namespace std;

int main()
{
 freopen( "A-large.in", "r", stdin );
 freopen( "outputlarge.out", "w", stdout );

 int i,t,n,a[10],j,cn,r;
 long int m;
 scanf("%d",&t);

 i=0;
 while(i<t)
 {
   scanf("%d",&n);

   if(n==0)
    printf("Case #%d: INSOMNIA\n",i+1);

   else
    {
     for(j=0;j<10;j++)
       a[j]=0;
     j=1;
     cn=0;
     while(cn<=9)
      {
       m=n*j;
       while(m)
       {
        r=m%10;
        if(a[r]==0)
        cn++;

        a[r]=1;
        m=m/10;
       }
       if(cn==10)
         {
          printf("Case #%d: %d\n",i+1,n*j);
         }
      j++;
      }
   }
   i++;
 }
}
