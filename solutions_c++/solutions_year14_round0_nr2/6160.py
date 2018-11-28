#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int t;
    cin >> t;
    cout << setprecision(7);
    for (int i = 1; i <= t; i++) {
        double c, f, x;
        double speed = 2.0;
        double time = 0.0;
        cin >> c >> f >> x;
        while (x > 0) {
            if (x / speed > c / f + c / speed) {
                time += c / speed;
                speed += f;
            } else {
                time += x / speed;
                break;
            }
        }
        cout << "Case #" << i << ": " << time << endl;
    }
}
