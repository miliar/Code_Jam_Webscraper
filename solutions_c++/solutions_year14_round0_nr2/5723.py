#include <iostream>
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;
int main()
{
    long double C, F, X;
    int T;
    long double time_to_make_farms, current_time, prev_time;
    long double farms_quantity;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ": ";
        cin >> C >> F >> X;
        time_to_make_farms = 0;
        farms_quantity = 0;
        current_time = X/(2.0);
        do {
                time_to_make_farms += C/(2.0 + farms_quantity * F);
                ++farms_quantity;
                prev_time = current_time;
                current_time = time_to_make_farms + X/(2 + farms_quantity * F);
        } while (prev_time >= current_time);
        cout.precision(7);
        cout << std::fixed << prev_time << endl;
    }
    return 0;
}
