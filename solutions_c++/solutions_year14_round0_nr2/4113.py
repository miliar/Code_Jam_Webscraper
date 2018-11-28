#include <iostream>
#include <iomanip>

using namespace std;

float work() {
    double farmCost, farmSpeed, target, currentSpeed = 2.0, currentTime = 0.0;
    cin >> farmCost >> farmSpeed >> target;
    while (true) {
        double remainingNow = target / currentSpeed;
        double remainingIf = target / (currentSpeed + farmSpeed) + farmCost / currentSpeed;
        if (remainingNow < remainingIf)
            return currentTime + target / currentSpeed;
        currentTime += farmCost / currentSpeed;
        currentSpeed += farmSpeed;
    }
}

int main(void) {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        cout << "Case #" << i << ": " << setprecision(15) << work() << endl;
    }
    return 0;
}