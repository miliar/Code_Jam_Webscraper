#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <vector>
#include <stack>
#include <iostream>
#include <string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;
signed long long check_palindrom(signed long long num)
{ 
     signed long long n,digit,rev=0;
     n=num;
     do
     {   digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;     
     }while (num!=0);
     if(n==rev) return n;
     return -1;
}


int main ()
{
        READ("C-small-attempt0.in");
        WRITE("C-out.out");
            
        int t ; 
        cin >> t;
        signed long long x,y,res;
        double sqr;
        long long cnt = 1;
        long long counter=0;
        while(cnt<=t)
        {
          counter=0;           
          cin>>x>>y;
          for(signed long long i=x ;i<=y ;i++)
          {
                     
                  res = check_palindrom (i);
                   if(res==-1)continue;
                  else 
                  {
                       
                   sqr= sqrt(res);
                   res= sqr;
                   if(sqr==res)
                   {
                       res = check_palindrom (res);
                       if(res!=-1) counter++;      
                   }    
                   else continue;
                  } 
          }
          cout<<"Case #" << cnt <<": " <<counter<<endl;
          cnt++;
                    
        }
        

return 0;
}


