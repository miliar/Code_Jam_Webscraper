#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int round = 1; round <= t; ++round) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << round << ":";
        for(int i = 1; i <= k; ++i) {
            cout << " " << i;
        }
        cout << endl;
    }
    return 0;
}

