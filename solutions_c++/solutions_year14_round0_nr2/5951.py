#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

double MinTime(double cost, double step, double gain, double goal) {
    double time_left_goal = goal / gain;
    double time_left_buy = cost / gain;
    if (time_left_goal <= time_left_buy + goal/(gain+step))
        return time_left_goal;
    else
        return time_left_buy + MinTime(cost, step, gain+step, goal);
}

int main() {
	int T;
    cin >> T;

    for(int i = 1; i <= T; ++i)
    {
        double c, f, x;
        cin >> c >> f >> x;
        printf("Case #%d: %.7f\n", i, MinTime(c, f, 2.0, x));
    }
	return 0;
}