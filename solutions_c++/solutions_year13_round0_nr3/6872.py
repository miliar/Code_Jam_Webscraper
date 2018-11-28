#include<iostream>
#include<math.h>
using namespace std;
int palindrome(int);
int main()
{
    int x,temp,c=0,i=1,a,b,f=0;
    
    cin>>x;
    
    while(x--)
    {
              f=0;
              cin>>a;
              cin>>b;
              a--;
              while((a)!=(b))
              {
                         a++;
                         c=sqrt(a);
                         if((c*c)!=a)
                         continue;
                         
                         if(palindrome(a) && palindrome(c))
                         {
                                          f++;
                                          }
                                          
                                          }
              cout<<"Case #"<<i<<": "<<f<<endl;
              i++;
              }
              }
                   
                                    
int palindrome(int temp)              
{int c;
c=0;
int x=temp;
    while(temp)
    {
               c=(c*10)+(temp%10);
               temp/=10;
              }
    if(c==x)
    return 1;
    
    else return 0;
}
