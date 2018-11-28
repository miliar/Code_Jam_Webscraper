#include<iostream>
#include<conio.h>
#include<math.h>
#include<cstdio>
#include<stdio.h>
using namespace std;
long long int reverse(int y)
{
    long long int sum=0;
    while(y>0)
    {
              long long int y1=y%10;
             sum=sum*10+y1;
             y=y/10;
             }
              return(sum);
              }
              int main()
              {
                  freopen("C-small-attempt2.in","r",stdin);
                    freopen("outp.in","w",stdout);
                  long long int T;
                  //cout<<"enter the no. of test cases";
                  cin>>T;
                  for(long long int r=1;r<=T;r++)
                  {
                         long long  int count=0,a,b,square;
                          //cout<<"enter the range of values"<<"\n";
                          cin>>a>>b;
                          for(long long int u=a;u<=b;u++)
                          {
                                  square=0;
                                  if(u==1)
                                  {
                                          count++;
                                          //cout<<"\n"<<u;
                                          }
                                          else
                                          {
                           for(long long int ff=1;ff<=u/2;ff++)
                           {
                                   if((ff*ff)==u)
                                   {
                                   square=ff;
                                   break;
                                   }}
                                   if(square!=0)
                                   {
                                   if(u==reverse(u)&&square==reverse(square))
                                  {
                                                   {
                                                   count++;
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   cout<<"Case"<<" #"<<r<<":"<<" "<<count<<"\n";
                                                   }
                                                 
                                                   getch();
                                                   return(0);
                                                   }
