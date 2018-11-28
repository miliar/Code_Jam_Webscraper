#include <iostream>
#include <iomanip>

int main() {
    int T;
    std :: cin >> T;
    for (int cas = 1; cas <= T; ++ cas) {
        double c, f, x;
        std :: cin >> c >> f >> x;
        double time = 0, add = 2;
        double ans = 1e100;
        for (int i = 0; i <= 100000000; ++ i) {
            ans = std :: min(ans, time + x / add);
            time += c / add;
            add += f;
        }
        std :: cout << "Case #" << cas << ": ";
        std :: cout.setf(std :: ios :: fixed);
        std :: cout.precision(7);
        std :: cout << ans << std :: endl;
    }
    return 0;
}
