#include <fstream>
#include <cmath>

using namespace std;

ifstream in("A-small-attempt0 (1).in"); ofstream out("A.out");

int T, l=1;
double r , t, dresult, delta;
unsigned long long result;
bool flag = false;

int main()
{
    in>>T;
    while(T--)
    {
          if (flag) out<<endl; flag = true;
          in>>r>>t;
          result =0;
          delta = ((2*r-1)*(2*r-1)+8*t);
          dresult = (-(2*r-1) + sqrt(delta))/4;
          result = dresult;
          out<<"Case #"<<l<<": "<<result;l++;
              }
    
    
    }
