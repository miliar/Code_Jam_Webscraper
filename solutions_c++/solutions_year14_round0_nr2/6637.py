#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;
    cout.precision(30);
    for (int test = 1; test <= cases; test++) {
        double c, f, x;
        cin >> c >> f >> x;

        double t = 0;
        double curinc = 2;
        while(true) {
            if (c / curinc > x / curinc) {
                t += x / curinc;
                break;
            }

            t += c / curinc;

            if (x / (curinc + f) > (x - c) / curinc) {
                t += (x - c) / curinc;
                break;
            }

            curinc += f;

        }
        cout << "Case #" << test << ": "  << t << endl;
    }
}