#include <cstdio>

using namespace std;

double solve() {
    double C,F,X;
    scanf("%lf %lf %lf", &C, &F, &X);

    double t = 0;
    double inc_ratio = 2;

    double opt_time = X / inc_ratio;

    for(int z = 0; z <= X/C; z++) {
        //z == number of buys
        inc_ratio = 2 + z * F;
        double time_to_reach_x_with_current_ratio = t + X / inc_ratio;
        
        if (time_to_reach_x_with_current_ratio < opt_time) {
            opt_time = time_to_reach_x_with_current_ratio;
        }
        if (time_to_reach_x_with_current_ratio > opt_time) break;


        // increase time (we had to buy a farm)
        t += C / inc_ratio; 
        

    }

    return opt_time;

}

int main () {
    int T;
    scanf("%d", &T);
    
    for (int testCase = 1; testCase <= T; testCase++){

        double result = solve();
        printf("Case #%d: %.7lf\n", testCase, result);
    }

    return 0;
}
