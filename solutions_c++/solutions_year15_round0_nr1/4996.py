//mdm

#include<iostream>
#include<stdio.h>

int main()
{
 int test;
 scanf("%d",&test);
 int maxi,i;
 char arr[1050];
 long long count,ans;
 int j;
 for(j=1;j<=test;j++)
 {
   scanf("%d",&maxi);
   count=0;
   ans=0;
   //for(i=0;i<maxi;i++)
   scanf("%s",arr);
   for(i=0;i<maxi+1;i++)
   {
    if(arr[i]!='0')
    {
      if(count<i)
      {
        ans=ans+i-count;
        count=i;
      }
      count=count+(arr[i]-'0');
    }
   }
   printf("Case #%d: %lld\n",j,ans);
 }  
// printf("Jai Mata Di");
 return 0;
}
