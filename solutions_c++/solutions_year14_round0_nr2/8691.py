#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;


int main (int argc, char const *argv[]) {
    long long T;
    fstream f("in.in");
    f >> T;
    For (t, T) {
        double C, F, X, dur = 0;
        f >> C;
        f >> F;
        f >> X;
        if (X <= C) {
            dur = X/2.0;
        }
        else {
            int buyTimes = ((X-C)/C) - 2/F + 1;
            For (k, buyTimes) {
                dur += C / (2 + k*F);
            }
            dur += X / (2 + buyTimes*F);
        }
        cout.precision(7);
        cout << "Case #" << t+1 << ": " << dur << endl;
    }
    f.close();
    return 0;
}
