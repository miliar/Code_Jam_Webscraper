#include <assert.h>

#include <iostream>
#include <iomanip>
using namespace std;

double calculate_time(double c, double f, double x, int farm_num)
{
    if(farm_num == 0) return x/2;
    double total_time = 0;
    for(int i = 0; i <= farm_num - 1; i ++) {
        total_time += (c / (2 + f * i));
    }
    total_time += (x / (2 + f* farm_num));

    return total_time;
}
int main()
{
    int tc, ori_tc;
    cin >> tc;

    ori_tc = tc;

    while (tc) {
        double c, f, x;
        cin >> c >> f >> x;

        int farm_num = x/c - 2/f + 5;
        farm_num -= 6;

        if(farm_num < 0) {
            double total_time = x/2;
            cout << "Case #" << ori_tc - tc + 1  << ": " << total_time << endl;
        }
        else {
            cout << setprecision(9) << "Case #" << ori_tc - tc + 1  << ": " 
                << calculate_time(c, f, x, farm_num + 1) << endl;
        }
        tc --;
    }
}
