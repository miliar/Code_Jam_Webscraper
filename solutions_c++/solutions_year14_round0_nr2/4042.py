#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        double c, f, x;
        int numFactories = 0;
        cin >> c >> f >> x;
        double timeToCatchUp = c/f;
        for (numFactories = 0; (timeToCatchUp + c/(2.0+(numFactories*f))) * (2.0 + (numFactories*f)) < x; numFactories++);
        double ans = x/(2.0+((numFactories)*f));
        for (int i = 0; i < numFactories; i++)
            ans += c/(2.0 + i*f);
        cout << fixed;
        cout << "Case #" << tc + 1<< ": " << setprecision(7) << ans << endl;
    }
    return 0;
}