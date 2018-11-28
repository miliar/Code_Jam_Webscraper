#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;


void alg() {
    double result(0);
    double C, F, X;
    cin >> C >> F >> X;
    
    double coockies(0);
    double cps(2.0);
    while (coockies < X) {
        if ((X - (coockies - C)) / (cps + F) < (X - coockies) / cps) {
            if (coockies >= C) {
                coockies -= C;
                cps += F;
            } else {
                result += (C - coockies) / cps;
                coockies = C;
            }
        } else {
            result += (X - coockies) / cps;
            coockies = X;
        }
    }
    
    cout << fixed << setprecision(7);
    cout << result << endl;
}

int main() {
    int n_cases(0);
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
