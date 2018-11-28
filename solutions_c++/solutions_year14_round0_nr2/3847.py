#define _USE_32BIT_TIME_T 1
#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

//typedef long double ldouble;

const double EPS = 1e-12;

double result(ifstream& cin)
{
    double C, F, X, F0 = 2., res = 0.;
    cin >> C >> F >> X;
    while (X * F > C * (F0 + F) + EPS) {
        res+= C / F0;
        F0+= F;
    }
    return res + X / F0;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    cout.precision(7);
    cout.setf(ios::fixed, ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": " << result(cin) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
