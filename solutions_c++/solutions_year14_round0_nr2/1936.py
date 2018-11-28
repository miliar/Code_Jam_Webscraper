#include <iostream>
#include <stdio.h>

using namespace std;

void process(int t, double c, double f, double x)
{
    double earn = 2;
    double ans = 0;
    double time_to_next_farm = c / earn;
    double time_to_x = x / earn;
    double time_to_x_by_farm = time_to_next_farm + x / (earn + f);

    while (time_to_x > time_to_x_by_farm) {
        ans += time_to_next_farm;
        earn += f;
        // update param
        time_to_next_farm = c / earn;
        time_to_x = x / earn;
        time_to_x_by_farm = time_to_next_farm + x / (earn + f);
    }
    ans += time_to_x;

    printf("Case #%d: %.7lf\n", t, ans);
}

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++) {
        double C, F, X;
        cin >> C >> F >> X;
        process(t, C, F, X);
    }
    return 0;
}
