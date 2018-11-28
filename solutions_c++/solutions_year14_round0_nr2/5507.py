#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    cout.precision(10);
    for (int case_num = 1; case_num <= t; ++case_num) {
        double c, f, x;
        cin >> c >> f >> x;

        double res = x;
        double now = 0;
        int f_num = 0;
        double cps = 2;
        while (islessequal(f_num, x)) {
            double tmp = now + x / cps;
            if (isless(tmp, res))
                res = tmp;
            now += c / cps;
            ++f_num;
            cps += f;
        }
        cout << "Case #" << case_num << ": " << res << "\n";
    }
    return 0;
}
