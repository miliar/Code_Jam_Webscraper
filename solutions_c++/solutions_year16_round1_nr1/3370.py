#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char str[1010],str1[2030];
int main()
{
    int t,k=1;
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    scanf("%d",&t);
    while(t--)
    {
       scanf("%s",str);
       int n=strlen(str);
       int i,z=n,y=n;
      // char str1[2*n+5];
       for(i=0;i<n;i++)
       {
          if(i==0)
          str1[z]=str[i];
          else
          {
             if(str[i]>=str1[y])
             {
               str1[y-1]=str[i];
               y--;
             }
             else
             {
                 str1[z+1]=str[i];
                 z++;
             }
          }
       }
       printf("Case #%d: ",k);
       for(i=y;i<=z;i++)
       printf("%c",str1[i]);
       printf("\n");
       k++;
    }
    return 0;
}  
       
    
