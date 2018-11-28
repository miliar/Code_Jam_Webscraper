#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <math.h>

using namespace std;

bool isqrt(int x)
{
     int y = sqrt(x);
     if(x == (y*y))
     {
          return true;
     }
     else
     {
         return false;
     }
}

bool ispali(int x)
{
     int n = x;
     int sz = 0;
     int o = 1;
     while(n>0)
     {
          n = n/10;     
          sz++;
          o = o * 10;     
     }
     o = o/10;
     n = x;
     int g = 0;
     for(int i = 0; i < sz; i++)
     {
          
          
          g = g + ((n%10)*o);
          //cout << g << " " << n<< endl;
          o = o/10;
          n = n/10; 
             
     }
     
     if(g == x)
     {
          return true;
     }
     else
     {
         return false;
     }
     
}

bool isfair(int x)
{
     if(isqrt(x))
     {
           int y = sqrt(x);      
           if(ispali(x) && ispali(y))
           {
                 return true;       
           }
           else
           {
               return false;
           }     
     }
     else
     {
        return false;
     }
}
int main(int argc, char *argv[])
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    
    /*int a = 4;
    int b = sqrt(a);
    cout << b;
    */
    int n;
    cin >> n;
    int a, b;
   
    for(int i = 0; i < n; i++)
    {
       cin >> a >> b; 
       int count = 0;
       for(int j = a; j <= b; j++)
       {
               if(isfair(j))
               {
                     count++;   
                     //cout << 45<<endl;    
               }
       }
       cout <<"Case #" <<i+1<<": "<< count<< endl;
    }
    
    
    /*int fa = 66;
    bool f = ispali(fa);
    if(f)
    {
         cout << "True";
    }
    else
    {
        cout << "false";
    }*/
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
