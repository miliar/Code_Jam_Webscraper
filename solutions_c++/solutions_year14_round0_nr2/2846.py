#include <iostream>
#include <cstdio>

using namespace std;

void run(double &C, double &F, double &X, double &rate, double &re)
{
    if (X <= C)
    {
        re += X / rate;
        return;
    }

    re += C / rate;
    double remain = (X-C) / rate;
    while (remain > X / (rate + F))
    {
        rate += F;
        re += C / rate;
        remain = (X-C) / rate;
    }
    re += remain;
    return;
}

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;

    for (int tt = 0; tt < T; ++tt)
    {
        double C, F, X;
        cin >> C >> F >> X;

        double re = 0;
        double rate = 2;

        run(C, F, X, rate, re);

        cout << "Case #" << tt+1 << ": " ;
        printf("%.7lf\n", re);
    }
    return 0;
}