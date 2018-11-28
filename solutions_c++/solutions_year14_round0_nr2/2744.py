#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
using namespace std;
int main()
{
    int t;
    double c,f,x;
    ifstream f_in("B-large.in");
    ofstream f_out("answer.out");
    f_in >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        f_in >> c >> f >> x;
        double psg = 2.0,ans = 0;
        if(x < c)
        {
            f_out <<"Case #"<<cas<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<x/psg<<endl;
        }
        else
        {
            while(x*psg < (x-c)*(psg+f)){
                ans += c/psg;
                psg += f;
            }
            ans += x/psg;
            f_out <<"Case #"<<cas<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<ans<<endl;
        }

    }
    return 0;
}
