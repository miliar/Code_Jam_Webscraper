#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

ifstream F("p.in");
ofstream G("p.out");

int T;
double cost,ploos,must,now,time;

int main()
{
    F>>T;
    for (int t=1;t<=T;++t)
    {
        F>>cost>>ploos>>must;
        now = 2;
        time = 0;
        while ( must / ( ploos + now ) + ( cost / now ) < (must / now) )
        {
            //cerr<<( must - cost )<<' ';
            //cerr<<must / ( ploos + now )<<' ';
            //cerr<<(cost/now)<<' ';
            //cerr<<(must / now)<<'\n';
            time = time + cost / now;
            now += ploos;
        }
        time += must / now;
        G<<"Case #"<<t<<": ";
        G<<fixed<<setprecision(7)<<time<<'\n';
    }
}
