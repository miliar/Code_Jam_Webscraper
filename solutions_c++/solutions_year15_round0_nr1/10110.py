#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{ int tc;
  scanf("%d",&tc);
  int i;
  for(i=1;i<=tc;i++)
   { printf("Case #%d: ",i);
     int length,j,sum1=0,sum2=0;
     scanf("%d",&length);
     char str[length+2];
     scanf("%s",str);
     int arr1[length+2],count=0,k,arr2[length+2];
     for(j=0;str[j]!='\0';j++)
       { arr1[j]=str[j]-'0';
         arr2[j]=arr1[j];
       }
     for(j=1;j<(length+1);j++)
      { if(arr1[j]!=0)
          { int sum=0;
            for(k=0;k<j;k++)
              { sum=sum+arr1[k];
              }
            if(sum<j)
             { count=count+j-sum;
               arr1[j-1]=arr1[j-1]+count;
               count=0;
             }
          }
      }
     for(j=0;j<(length+1);j++)
      { sum1=sum1+arr1[j];
       sum2=sum2+arr2[j];
      }
     int result=sum1-sum2;
         printf("%d\n",result);
   }
  return 0;
}