#include <iostream>
#include <fstream>
#include <iomanip>

int main ()
{
    std::ifstream fin("cookie.in");
    std::ofstream fout("cookie.out");
    int t;
    double c,f,x,best;

    fin>>t;
    for(int i=1;i<=t;i++)
    {
        fin>>c>>f>>x; 
        double besttime, time=0;
        double rate = 2.0;
        best = x/rate;
        for(int k=1;;k++)
        {
            time+=c/rate;
            rate+=f;
            if(time + x/rate < best)
            {
                best = time + x/rate;
            } 
            else
            {
                break; 
            }
        }
        fout<<std::setprecision(16)<<"Case #"<<i<<": "<<best<<std::endl;
    }
 
    return 0;
}
