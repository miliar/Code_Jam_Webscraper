#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int l0 = 0; l0 < t; l0++) {
        double tot = 0;
        double c, f, x;
        cin >> c >> f >> x;
        double cur = 2.0;
        double time = x / cur;
        while ((x / cur) > ((c / cur) + (x / (cur + f)))) {
            tot += c / cur;
            cur += f;
        }
        cout << "Case #" << l0 + 1 << ": " << fixed << setprecision(7) << tot + x / cur << '\n';
    }
    return 0;
}
