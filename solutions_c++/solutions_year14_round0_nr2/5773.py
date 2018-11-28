#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("input.txt","r",stdin);
    cout << fixed << setprecision(7);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        double C, F, X, ttime = 0, cprod = 2;
        cin >> C >> F >> X;
        while (true) {
            double t1 = X/cprod;
            double t2 = C/cprod + X/(cprod+F);
            //cout << t1 << "-" << t2 << endl;
            if (t1 < t2) {
                ttime += t1;
                break;
            } else {
                ttime += C/cprod;
                cprod += F;
            }
        }

        cout << "Case #" << tc << ": " << ttime << endl;

    }
}
