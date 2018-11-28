#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <memory.h>
#include <assert.h>
using namespace std;

ifstream fin;
ofstream fout;

double C, F, X;
double res;
int testNum;

void init();
void solve();
void output(int T);

int main()
{
    int T;
    fin.open("B-large.in");
    fout.open("B-large.out");
    fin >> testNum;
    for (T=1; T<=testNum; T++)
    {
        init();
        solve();
        output(T);
    }
    fin.close();
    fout.close();
    return 0;
}

void init()
{
    fin >> C >> F >> X;
}

void solve()
{
    double rate, cookies, spent;
    res = 0;
    rate = 2.00; cookies = C; spent = C/rate;
    if (C>=X)
    {
        res = X/rate;
        return;
    }

    // assume that C < X
    while (cookies < X)
    {
        double tmp1, tmp2;
        tmp1 = (X-C)/rate;
        tmp2 = X/(rate+F);
        if (tmp1 < tmp2)
        {
            // don't buy a farm
            cookies = X;
            spent += tmp1;
            break;
        }
        else
        {
            // buy a farm
            cookies = C;
            rate += F;
            spent += C/rate;
        }
    }
    res = spent;
}

void output(int T)
{
    fout << "Case #" << T << ": ";
    //fout << setprecision(7) << res << endl;
    fout << setprecision(7) << setiosflags(ios::fixed|ios::showpoint) << res << endl;

}
