#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int cas = 1; cas <= n; cas++) {
        double c, f, x, rate = 2., time = 0.;
        cin >> c >> f >> x;
        while (1) {
            if (x/rate > (x)/(rate+f) + c/rate) {
                time += c/rate;
                rate += f;
                continue;
            }
            time += x/rate;
            break;
        }
        cout << "Case #" << cas << ": " << setprecision(7) << fixed << time << endl;
    }
}