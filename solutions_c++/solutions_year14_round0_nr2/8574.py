#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip> 

using namespace std;

int main() 
{
    ifstream inputf("B-small-attempt0.in");
    ofstream output("ans.txt");
    int t;
    double c,f,x;
    inputf >> t;
    for(int i=0;i<t;i++)
    {       
       inputf >> c >> f >> x;
       double temp1 = c/2 + x/(2+f);
       double temp = x/2;
       if(temp>temp1)
       {
           temp = temp1;
           double k=1;
           while(1)
           {
               temp1 = temp + (c-x)/(2+k*f) + x/(2+(k+1)*f);
               if(temp>temp1)
               temp = temp1;
               else 
               break;
               k++;
           }           
       }
       output <<"Case #"<<i+1<<": "<< setprecision(9)<<temp << endl;
    }     
    return 0;
}
