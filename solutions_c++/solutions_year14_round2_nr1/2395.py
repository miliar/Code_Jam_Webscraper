#include<algorithm>
#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#define MAX 101
using namespace std;
int main()
{
    int t, c, d, n, num, i, j, l1, l2, cnt;
    char s1[MAX], s2[MAX], a, b, temp;
    cin>>t;
    for(num=1; num<=t; num++)
    {
               c=0, i=0, j=0, cnt=0;
               temp=' ';
               cin>>n;
               cin>>s1;
               cin>>s2;
               l1=strlen(s1);
               l2=strlen(s2);
               if(strcmp(s1, s2)==0)
               {
                             c=1;
                             cnt=0;
               }
               else
               {
                   do
                   {
                             a=s1[i];
                             b=s2[j];
                             if(a==b)
                             {
                                     i++;
                                     j++;
                                     temp=a;
                             }
                             else if(a!=b && a!=temp && b==temp)
                             {
                                  i--;cnt++;
                             }
                             else if(a!=b && a==temp && b!=temp)
                             {
                                  cnt++;
                                  j--;
                             }
                             else if(a!=b && a!=temp && b!=temp)
                             {
                                  break;
                             }
                             if(i==l1 && j==l2)
                             {
                                      c=1;
                                      break;
                             }
                   }while(1);
               }
               if(c==0)
               {
                       cout<<"Case #"<<num<<": Fegla Won\n";
               }
               else
               {
                   cout<<"Case #"<<num<<": "<<cnt<<"\n";
               }
    }
    
    return 0;
}                                 
               
               
             
