#include <iomanip>
#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int main(void)
{
    int T;

    cin >> T;
    for (int t = 1; t <= T; t++){
        double C, F, X, tw, tf;
        double a = 2.0;
        cin >> C >> F >> X;
        tw = X/a;
        tf = C/a + (X/(a + F));
        double T = 0;
        while (tw > tf){
            T += C/a;
            a += F;

            tw = X/a + T;
            tf = C/a + (X/(a + F)) + T;
        }
        cout << "Case #" << t << ": " << fixed << setprecision(7) << tw << endl;

    }

    return 0;
}
