#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        double C, F, X;
        cin >> C >> F >> X;
        double speed = 2.0;
        double result = X / speed;
        double time = C / speed;
        for (speed += F; time + X / speed < result; speed += F) {
            result = time + X / speed;
            time += C / speed;
        }
        cout.precision(15);
        cout << result;
        cout << endl;
    }
}
