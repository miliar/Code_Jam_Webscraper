#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int Z;
    cin >> Z;
    for( int test = 1; test <= Z; test++ ) {
        long double c,f,x;
        cin >> c >> f >> x;
        long double income = 2;
        long double best = x/income;
        long double ctime = 0;
        for(int i = 0; i < 10000000; i++) {
            ctime += c/income;
            income += f;
            best = min(best,x/income+ctime);
        }
        cout << "Case #" << fixed << setprecision(7) << test << ": " << best << endl;
    }
    return 0;
}

