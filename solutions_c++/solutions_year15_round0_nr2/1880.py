#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int d;
        cin >> d;
        vector<int> p(d);
        for (int i = 0; i < d; i++) cin >> p[i];
        int minTime = 1000;
        for (int m = 1; m <= 1000; m++) {
            int k = 0;
            for (int i = 0; i < d; i++) {
                k += (p[i] - 1) / m;
            }
            minTime = min(minTime, k + m);
        }
        cout << "Case #" << testCase << ": " << minTime << endl;
    }
    return 0;
}
