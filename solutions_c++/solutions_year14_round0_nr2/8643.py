#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <map>
#include <cassert>
#include <iomanip>  

using namespace std;

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    double C, F, X;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> C >> F >> X;

        double total_time = 0;
        for (int a = 0; a <= X / C + 1; ++a) {
            if (X / (2 + F * a) <= (X / (2 + F * (a + 1)) + C / (2 + F * a)) ) {
                total_time += X / (2 + F * a);
                break;
            } else {
                total_time += C / (2 + F * a);
            }
        }
        cout << "Case #" << t + 1 << ": " << std::fixed << std::setprecision(7) << total_time << std::endl;
    }

    return 0;
}