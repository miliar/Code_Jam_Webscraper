#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        long double time = 0, x, f, c, speed = 2;
        cin >> c >> f >> x;
        while(time + x/speed > time + c/speed + x/(speed + f)) {
            time += c/speed;
            speed += f;
        }
        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(7) << time + x/speed;
        cout << '\n';
    }

    return 0;
}
