#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<conio.h>

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    int t=0;
    while(T--)
    {
              t++;
              int w=0,wd=0;
              int s;
              scanf("%d",&s);
              double a[s],b[s];
              int i,j;
              for(i=0;i<s;i++)
              scanf("%lf",&a[i]);
              
              for(i=0;i<s;i++)
              scanf("%lf",&b[i]);
              
              sort(a,a+s);
              sort(b,b+s);
              
              i=0;
              j=0;
              while(i<s&&j<s)
              {
                             if(a[i]<b[j])
                             {
                                          i++;
                                          j++;
                                          w++;
                                          
                                          }
                             else
                             {
                             j++;
                             //w++;
                             
                             }
              }
              
              for(i=0;i<s;i++)
              for(j=0;j<s;j++)
              {
                             if(a[i]>b[j]&&a[i]!=-1&&b[j]!=-1)
                             {
                                 wd++;
                                 a[i]=-1;
                                 b[j]=-1;
                                 }
                                 }
                                 
             cout<<"Case #"<<t<<": "<<wd<<" "<<s-w<<endl;                    
                                 
                                 }
                                 getch();
                                 }                     
