#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int t, smax;
    string s;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cin >> smax;
        cin >> s;
        int claps = 0, adds = 0;
        for (int j = 0; j <= smax; j++) {
            if (claps < j) {
                adds += j - claps;
                claps += j - claps;
            }
            claps += atoi(s.substr(j,1).c_str());
        }
        cout << "Case #" << i << ": " << adds << endl;
    }
    return 0;
}
