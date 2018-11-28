#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

ifstream in("cookie.in");
ofstream out("cookie.out");

void solve(int i){
    double farmCost, farmRate, req;
    double rate = 0;
    in>>farmCost>>farmRate>>req;
    double time = farmCost / 2;
    double minTime = req / 2 ;
    rate = 2 + farmRate;
    while(time<minTime){
        minTime = min(minTime, time + req/rate);
        time += farmCost/ rate;
        rate+= farmRate;
    }

    out<<"Case #"<<i<<": ";
    out<<fixed;
    out<<setprecision(7)<<minTime;
    out<<"\n";
}

int main()
{
    int t;
    in>>t;

    for(int i=1;i<=t;i++){
        solve(i);
    }
    return 0;
}
