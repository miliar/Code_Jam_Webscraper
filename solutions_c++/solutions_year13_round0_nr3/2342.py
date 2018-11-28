#include<iostream>
#include<conio.h>
#include<math.h>
#include<cstdio>
#include<stdio.h>
using namespace std;
unsigned long long int reverse(unsigned long long int y)
{
    unsigned long long int sum=0;
    while(y>0)
    {
             unsigned long long int y1=y%10;
             sum=sum*10+y1;
             y=y/10;
             }
              return(sum);
              }
              int main()
              {
                 unsigned long long arr[50];
                 int count=0;
                  freopen("C-large-1.in","r",stdin);
                    freopen("outclong.in","w",stdout);
                  unsigned long long int T;
                  //cout<<"enter the no. of test cases";
                  for(unsigned long long int u=1;u<=(sqrt(pow(10,14))+1);u++)
                          {
                          
                                   
                                   if((u==reverse(u))&&((u*u)==reverse(u*u))&&((u*u)<=(pow(10,14))))
                                  {
                                  
                                                   arr[count]=(u*u);
                                                   count++;
                                                   }
                                                   }
                           
                                      cin>>T;
                  for(unsigned long long int r=1;r<=T;r++)
                  {
                         unsigned long long  int count1=0,a,b;
                          
                          cin>>a>>b;
                          for(unsigned long long int ff=0;ff<count;ff++)
                          {
                                       if(arr[ff]>=a&&arr[ff]<=b)
                                       count1++;
                                       }
                   
                                      cout<<"Case"<<" #"<<r<<":"<<" "<<count1<<"\n";
                                                   
                                                   } 
                                                   getch();
                                                   return(0);
                                                   }
