#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

int main () {
  double c, f, g, r, t2goal, t2f, twf, current, newt;
  bool flag = false;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {
    cout << fixed << setprecision(7);
   int tests;
   myfile >> tests;
   for(int i = 0; i < tests; i++)
   {
       flag = false;
       myfile >> c >> f >> g;
       r = 2.000000;
       t2f = 0.0000;
       current = 0.000;
       newt = 0.000;
       
       do
       {
           current = g / r + t2f;
           t2f += c/r;
           newt = t2f + (g / (r +f));
           
           if(newt < current)
           {
               current = newt;
               r += f;
           }
           else
           {
               flag = true;
           }
           
       }while(!flag);
        cout <<"Case #" << i+1 << ": " << current << endl;
    
       
   }
   
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}