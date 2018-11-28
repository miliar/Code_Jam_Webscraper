#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std;

double solute(double c,double f,double x);

int main()
{

    int T;
    int times = 1;
    double C,F,X;

    ifstream myin("B-large.in");
    ofstream myout("result.txt");

    myin >> T;
    while(times++ <= T){
        myin >> C >> F >> X;
        myout << "Case #"<<times-1<<": ";
        myout.setf(ios::fixed);
        myout << setprecision(7) << solute(C,F,X) << endl;
    }

    return 0;
}

double solute(double c,double f,double x)
{
    double rate = 2;
    double ret = 0;

    while(c/rate+x/(rate+f) < x/rate){
        ret += c/rate;
        rate = rate + f;
    }
    ret += x/rate;
    return ret;
}
