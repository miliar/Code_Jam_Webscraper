#include<iostream>
#include<fstream>
#include<stdio.h>
#include <iomanip>
using namespace std;
int main()
{
    ifstream min ("Cbig.in");
    ofstream mout ("Cookie_result_big.txt");
    int t;
    min>>t;
    for(int i=0;i<t;i++)
    {
            long double c,f,x,tot=0.0000000,r=2.0000000;
            min>>c>>f>>x;
            //cout<<(c/r)+(x/(r+f));
            //cout<<endl<<(x/r)<<endl;
            while((c/r)+(x/(r+f))<(x/r))
            {
                                      tot=tot+(c/r);
                                      r=r+f;
                                      
                                      }
                                      
                                      tot=tot+(x/r);
                                      mout<<setprecision(10)<<"Case #"<<i+1<<": "<<tot<<endl;
            }
            system("pause");
            return 0;
            
}
