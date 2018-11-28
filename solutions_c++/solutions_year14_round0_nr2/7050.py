#include <iostream>
#include <cstdio>

using namespace std;

const int maxFarms = 1e6;

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        double c, f, x;
        cin >> c >> f >> x;
        double cur_speed = 2.0;
        double b_ans = x / cur_speed, pr_ans = 0;
        for (int i = 1; ;++i) {
            double t_ans = pr_ans + c / cur_speed;
            cur_speed += f;
            pr_ans = t_ans;
            t_ans += x / cur_speed;
//            cerr << t_ans << endl;
            if (t_ans > b_ans)
                break;
            else b_ans = t_ans;
        }

        printf("Case #%d: %.7f\n", test, b_ans);
    }
}
