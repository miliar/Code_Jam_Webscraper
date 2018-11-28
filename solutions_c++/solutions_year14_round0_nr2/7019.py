#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <list>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    int t;
    cin >> t;
    cout.precision(7);
    cout << fixed;

    for (int k = 1; k <= t; k++) {
        long double c,f,x;
        cin >> c >> f >> x;
        long double time = 0.0;
        long double rate = 2.0;

        while(1) {
            long double t1 = (c / rate);
            long double t2 = (x /(rate+f));
            long double y = x / rate;

            if ( t1+t2 < y) {
                time = time + t1;
                rate = rate + f;
            } else {
                break;
            }
        }

        long double temp = x / rate;
        time = time + temp;

        cout << "Case #" << k << ": " << time << endl;
    }

    return 0;
}
