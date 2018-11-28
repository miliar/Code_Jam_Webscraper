#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    cout << setprecision(9);
    int T;
    cin >> T;
    int N = 0;
    while (N < T) {
        N++;
        cout << "Case #" << N << ": ";
        double C, F, X;
        cin >> C >> F >> X;
        double cTime = 0;
        double cRate = 2;
        while (true) {
            double timeTillReady = (X / cRate);
            double timeNewFarm = (C / cRate) + (X / (cRate + F));
            if (timeTillReady > timeNewFarm) {
                cTime += (C / cRate);
                cRate += F;
            } else {
                cTime += (X / cRate);
                cout << cTime << endl;
                break;
            }
        }
    }
}
