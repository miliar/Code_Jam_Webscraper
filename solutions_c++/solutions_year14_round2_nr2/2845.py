#include<stdio.h>
#include<stdlib.h>
long int ar[20009]={0};
int main()
{
     long int i,j,k,l,m,n,p,q,t,a,b;
     scanf("%ld",&t);
     for(p=0;p<t;p++)
     {
                     scanf("%ld%ld%ld",&a,&b,&k);
                     for(i=0;i<20009;i++)
                     ar[i]=0;
                     for(i=0;i<a;i++)
                     {
                                     for(j=0;j<b;j++)
                                     {
                                                     l=i&j;
                                                     ar[l]++;
                                     }
                     }
                     m=0;
                     for(i=0;i<k;i++)
                     {
                                     m+=ar[i];
                     }
                     printf("Case #%ld: %ld\n",p+1,m);
     }
     system("pause");
     return(0);
}
