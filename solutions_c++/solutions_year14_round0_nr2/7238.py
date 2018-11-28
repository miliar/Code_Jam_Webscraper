#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin("CC.in");
ofstream fout("CookieClickerAlpha.out");

int nr;
double pretfarm,extra,total,timp;
double extracrt=2.0;

void rezolvare()
{
    timp=0;
    extracrt=2.0;
    fin>>pretfarm>>extra>>total;
    while(1)
    {
        double tdc=total/(extra+extracrt)+pretfarm/extracrt,tdnc=total/extracrt;
        if(tdc<tdnc)
        {
            timp+=pretfarm/extracrt;
            extracrt+=extra;
            //timp+=total/extracrt;
        }
        else
        {
            timp+=total/extracrt;
            break;
        }
    }
    fout << setprecision (7) << fixed << timp;
}

int main()
{
fin>>nr;
for(int i=1;i<=nr;i++)
{
    fout<<"Case #"<<i<<": ";
    rezolvare();
    fout<<endl;
}
    return 0;
}
