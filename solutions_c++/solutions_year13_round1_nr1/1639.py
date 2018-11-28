#include <iostream>

using namespace std;

#define PI 3.14159265359

long long int Solve(double r, double t)
{
    long long int num_of_black_discs = 0;
    long long int i = 1;
    while (1) {
        //inner_black_circle_r = outer_black_circle_r - 1;
        double area_diff_by_pi = 2.0 * (r + i) - 1.0;
        t -= area_diff_by_pi;
        //cout << "t= " << t << endl;
        if (t >= 0.0)
            ++num_of_black_discs;
        else
            break;
        i += 2;
    }
    return num_of_black_discs;
}


int main(void)
{
    int T;
    cin >> T;
    int i = 1;
    while (T--) {
        double r, t;
        cin >> r >> t;
        
        cout << "Case #" << i++ << ": " << Solve(r, t) << endl;
    }
    return 0;
}
