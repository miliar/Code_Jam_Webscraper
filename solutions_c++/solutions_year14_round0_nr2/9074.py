#include <string>
#include <fstream>
#include <iomanip> 
using namespace std;

int main () {
  ifstream input("B-large.in");
  ofstream output ("outputBeta.txt"); 
  int t=0;
   
  if (input.is_open())
  {      
    input>>t;
    for (int k = 1; k <= t; k++)
    {
        double c,f,x,time,rate = 2,timeElapsed = 0;
        input>>c>>f>>x; 
         
        //slowest time it'll take
        time = x/rate; 
        //find if waiting to buy a farm reaching x is faster
        while (x/(rate+ f) + c/rate + timeElapsed < time)
        {
         time = x/(rate+ f) + c/rate + timeElapsed;
         timeElapsed +=  c/rate; 
         rate += f; 
         
        }
        
         
         output<<"Case #"<<setprecision(10)<<k<<": "<<time<<"\n";
         
    }            
    
  }
  
  
  return 0;
}
