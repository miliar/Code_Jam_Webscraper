#include <iostream>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>

#define LEN 1000005

using namespace std;

void solve() {
    string pancakes;
    cin >> pancakes;

    long long result = 0;
    char lastPanckake = pancakes[0];

    for (auto pancake : pancakes) {
        if (pancake != lastPanckake) {
            ++result;
            lastPanckake = pancake;
        }
    }

    if (lastPanckake == '-') {
        result++;
    }

    cout << result << endl;
}

int main() {
    int numCases = 0;
    cin >> numCases;
    
    for (int testCase = 1; testCase <= numCases; ++testCase) {
        cout << "Case #" << testCase << ": ";
        solve();
    }
    
    return EXIT_SUCCESS;
}
