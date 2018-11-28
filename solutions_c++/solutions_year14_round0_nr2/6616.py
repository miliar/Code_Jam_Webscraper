#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
using namespace std;


double solve(double c, double f, double x)
{
    double speed = 2.0;
    double time = 0.0;
    for (int i = 0; c / speed + x / (speed + f) < x / speed; ++i) {
        time += c / speed;
        speed += f;
    }
    return time + x / speed;
}


int main()
{
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        double c, f, x;
        cin >> c >> f >> x;
        cout.precision(10);
        cout << "Case #" << test << ": " << solve(c, f, x) << endl;
    }
}
