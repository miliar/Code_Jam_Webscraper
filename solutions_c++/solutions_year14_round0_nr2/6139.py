#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    ifstream input("input23.txt");
    ofstream output;
    output.open("output23.txt");
    int t;
    input>>t;
    for(int i = 0; i < t; ++i)
    {
        double C,F,X;
        double R = 2.0;
        input>>C>>F>>X;
        double tt = 0.0;
        double lt = X / R;
        double ot = C / R + X / (R + F);
        while(ot < lt)
        {
            tt += (C / R);
            R += F;
            lt = X / R;
            ot = C / R + X / (R + F);
        }
        tt += lt;
        //output.precision(7);
        output<<"Case #"<<(i+1)<<": ";
        output<<fixed<<setprecision(7)<<tt;
        output<<endl;
    }
    output.close();
    return 0;
}

