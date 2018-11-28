#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        string S;
        cin >> S;
        string result;
        char currentMax;
        result += S[0];
        currentMax = S[0];
        for (int j = 1; j < S.size(); j++) {
            if(S[j] >= currentMax) {
                result = S[j] + result;
                currentMax = S[j];
            } else {
                result = result + S[j];
            }
        }
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}