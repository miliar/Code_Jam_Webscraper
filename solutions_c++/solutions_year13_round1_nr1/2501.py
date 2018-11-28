#include<iostream>
using namespace std;
int main()
{
   freopen( "A-small-attempt3.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
    int test,r,t,i,count,temp,n,x=1;
    cin>>test;
    while(test--)
    {           
               cin>>r>>t;
               n=t;
               count=0,i=r;
               while(n>0)
               {
                      temp=(2*i)+1;
                      i+=2;
                      n=n-temp;
                      count+=1;      
               }
               if(n<0)
               count-=1;  
               cout<<"Case #"<<x<<": "<<count<<endl;  
               x++;     
    }
 // system("pause");
 }
