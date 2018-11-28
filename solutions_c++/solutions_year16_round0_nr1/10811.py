#include<iostream>
#include<stdio.h>
int main()
{
   FILE *ip,*op;
    ip=fopen("A-large.in","r");
    op=fopen("A.in","w");
  long long int t,n,m,i,j,d,num;
   fscanf(ip,"%lld",&t);
   for(i=1;i<=t;i++)
   {
      int a[10]={0};
      fscanf(ip,"%lld",&n);
      j=0;
      if(n==0)
      {
         fprintf(op,"Case #%d: INSOMNIA\n",i);
         continue;
      }
      while(1)
      {
         int p,count=0,back;
         for(p=0;p<10;p++)
            if(a[p]==0)
            count++;
         if(count==0)
            break;
         num=(j+1)*n;
         m=num;
         while(m>0)
         {
            d=m%10;
            m=m/10;
            a[d]++;
         }
        j++;
      }

      fprintf(op,"Case #%d:",i);
      fprintf(op," %d\n",num);
   }
   fclose(ip);
    fclose(op);
    return 0;
}
