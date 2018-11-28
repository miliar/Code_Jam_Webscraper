#include <cstdio>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;
const int MAXITER = 100005;

int main() {
    ifstream cin("test.in");
    ofstream cout("test.out");

    int T; cin >> T;

    cout << setprecision(20) ;
    for (int testcase = 1; testcase <= T; ++testcase) {
        double C, F, X;
        cin >> C >> F >> X;

        double answer = 1 << 30 ;

        double fpower = 2;
        double spent_time = C/2;


        answer = min ( answer, max(0.0, X / 2) );
        for (int iter = 1; iter < MAXITER; ++iter) {
            answer = min (answer, X / (fpower+F) + spent_time );
            fpower += F;
            spent_time += C/fpower;
        }
        cout << "Case #" << testcase << ": " << answer << "\n";
    }

}

