#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

int T;
double C,F,X;

void init()
{
    cin >> C >> F >> X;
}

void solve()
{
    double unitget = 2;
    double time = 0;
    double best = X / unitget;
    while (true)
    {
        double t1 = C / unitget;
        if (t1 + time + X/(unitget + F) > best)
        {
            cout << setprecision(8) << best ;
            return;
        }
        time = time + t1;
        unitget = unitget + F;
        best = time + X / unitget;
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        init();
        solve();
        cout << endl;
    }
    return 0;
}
