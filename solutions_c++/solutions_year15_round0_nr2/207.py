#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long D;
        cin >> D;
        long diners[1000];
        for (int i = 0; i < D; i++) cin >> diners[i];
        long best = 999999999;
        for (int normal = 1; normal <= 1000; normal++) {
            long sum = 0;
            for (int i = 0; i < D; i++) {
                sum += (diners[i] - 1) / normal;
            }
            best = min(best, sum + normal);
        }
        cout << "Case #" << t << ": " << best << endl;
    }
}
