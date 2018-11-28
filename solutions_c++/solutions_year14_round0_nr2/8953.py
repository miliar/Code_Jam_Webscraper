#include <iostream>

using namespace std;

void solve(int testNum)
{
    double c, f, x;
    cin >> c >> f >> x;
    double cur_sum = 0;
    double res = 1e9;
    for (int cnt = 0; ; ++cnt) {
        double new_res = x / (2 + f * cnt) + cur_sum;
        if (new_res >= res - 1e-8) {
            break;
        }
        res = new_res;
        cur_sum += c / (2 + f * cnt);
    }
    cout << "Case #" << testNum <<": " << res << "\n";
}

int main()
{
    cout.setf(ios::fixed);
    cout.precision(42);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        solve(i + 1);
    }
    return 0;
}
