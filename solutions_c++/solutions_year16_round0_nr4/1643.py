#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector> 
#include <cstdint>
#include <cmath>

using namespace std;



int main(int argc, char **argv) {
    int tests;
    cin >> tests;

    for (int i = 1; i <= tests; i++) {
        unsigned int k, c, s;
        cin >> k >> c >> s;

        cout << "Case #" << i << ": ";


        if (k == 1) {
            cout << "1" << endl;
        } else if (k == s) {
            for (int j = 1; j <= k; j++) {
                cout << j << " ";
            }
            cout << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}



