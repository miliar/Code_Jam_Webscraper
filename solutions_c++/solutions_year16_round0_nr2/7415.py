#include <iostream>
#include <string.h>
#include<conio.h>
#include<stdio.h>
using namespace std;

 int main()
 {
     int t;
     char s[102];
     cin>>t;
     int h=1;
     int count =1;
         char check=s[0];
         int i=1;
     while(t--)
     {

         scanf(" %s" , s);
          count =1;
          check=s[0];
         i=1;
         while(s[i++]!='\0')
         {
             if(s[i-1]!=check)
             {
                 check = s[i-1];
                 count++;
             }
         }
         if(s[strlen(s)-1]=='-')
         printf("Case #%d: %d\n",h,count);
         else
          printf("Case #%d: %d\n",h,count-1);

h++;

     }
 }
