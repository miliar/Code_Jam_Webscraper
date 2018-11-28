#include <iostream>
#include <stack>
#include <sstream>
#include <cmath>
#include <stdio.h>
using namespace std;
int d ;
void f (string x )
{


         stack<char>s ;
        for (int i = 0 ; i < x.size() ; i++)
    {
            s.push(x[i]);
    }
    while (!s.empty())
    {

           if ( s.top() == x[0])
           {
                   x.erase(0,1);
                   s.pop();
           }
           else
           {

                   break ;
           }
    }
    if (s.empty())
    {
            d++ ;
    }
    else
      {
        d-- ;
      }
}

int main()
{

        freopen("C-small-attempt4.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
    freopen("output.txt", "wt", stdout); // same for out.txt
   int i =0 ;
   int p = 0 ;
   int q ;
   cin >> q ;
    int x , y ;


   for (int z = 0 ; z < q ; z++)
   {

   cin >> x >> y  ;
   while (x <=  y ){

    string x1 , y1 ;
    stringstream ss ;
    stringstream cs ;
    ss << x ;
    ss >> x1 ;


    f (x1);
    float n = sqrt ( x ) ;
      if( (int)n - n == 0)
      {
       cs << n ;
    cs >> y1 ;
    f(y1);
      }
      else
      i++ ;



       if (d == 2 )
   {
           p++;
   }
   else{
    i++ ;
   }
     x++ ;
    d = 0 ;

   }


   cout<<"Case #"<<z+1<<": "<<p<<endl;
   p = 0 ;
   }




    return 0;
}
