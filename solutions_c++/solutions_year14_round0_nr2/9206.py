#include<iostream>
#include<vector>
#include<fstream>
#include<set>
using namespace std;
int main()
{
    ifstream filein;
    ofstream fileout;
    filein.open("B-large.in");
    fileout.open("B-large.out");
    int t;
    filein>>t;
    for(int tc=1;tc<=t;tc++)
    {
            double C,F,X;
            filein>>C>>F>>X;
            double time=0.0000000;
            double rate=2.0000000;
            double min_time=X;min_time/=rate;
            while(true)
            {
                   time+=(C/rate);
                   rate+=F;
                   double z=X/rate;
                   if(time+z<min_time)       min_time=time+z; 
                   else break;                  
            }
            fileout.precision(10);
            fileout<<"Case #"<<tc<<": "<<min_time<<"\n";
    }
    filein.close();
    fileout.close();
    return 0;
}
