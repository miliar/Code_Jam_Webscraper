#include <iostream>
#include <fstream>
#include <iomanip>
#define ld long long int
using namespace std;
int main()
{
    ifstream romeo;
    ofstream rumon;
    romeo.open("B-large.in");
    rumon.open("B-large.out");
    double c, f, x, time, t;
    ld tc, i;
    romeo>>tc;
    for(i=1;i<=tc;i++)
    {
        time=0.0;
        t=2.0;
        romeo>>c>>f>>x;
        for(;;)
        {
            if((c/(t*1.0)+x/((t+f)*1.0))>=(x/(t*1.0)))
            {
                time+=(x/(t*1.0));
                break;
            }
            time+=(c/(t*1.0));
            t+=f;
        }
        //printf("%0.7lf\n", time);
        rumon<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
}
