#include <iostream>
#include <stdio.h>
#include <string.h>


int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   int tcase,mx,pl,len,sum,cnt,temp,i,casecount;
   char arr[10000];
   scanf("%d",&tcase);
   casecount=0;

   while(tcase--)
   {
       scanf("%d",&mx);
       scanf("%s",&arr);
       len=strlen(arr);

       sum=0;
       cnt=0;

       for(i=0;i<len;i++)
       {
           pl=(int)arr[i]-48;



           if(sum>=i)
           {
               sum=sum+pl;
           }
           else
           {
               temp=i-sum;

               cnt=cnt+temp;

               sum=sum+temp;

               sum=sum+pl;
           }

           //printf("people=%d sum=%d count=%d\n",pl,sum,cnt);
       }
       casecount++;
       printf("Case #%d: %d\n",casecount,cnt);
   }

   return 0;
}
