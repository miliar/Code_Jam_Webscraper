#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;


double solve(double C, double F, double X) {
    double cookies = 0;
    double time = 0;
    double rate = 2; // starting rate
    double time_till_intersection = C/F;// point at which trajectories intersect
    while(cookies <=X) {
        double time_till_next = (C - cookies)/rate;
        double time_till_win = (X - cookies)/rate;

        if(time_till_win <= time_till_next) { // not possible to buy another farm anyways
            return time + time_till_win;
        } else {
            time += time_till_next;
            cookies += rate*time_till_next;
            // now decide whether we should keep going or invest

            time_till_win = (X - cookies)/rate;
            if(time_till_intersection < time_till_win) {
                // invest
                cookies = 0;
                rate += F;
            } else { // finish it off
                return time += time_till_win;
            }

        }



    }

    return time;
}


int main() {
    int num_p;
    double C;
    double F;
    double X;
    cin >> num_p;
    for(int i = 1; i <= num_p; ++i) {
        cout << "Case #" << i<< ": ";
        cin >> C;
        cin >> F;
        cin >> X;
        double sol = solve(C,F,X);
        printf("%.7lf\n", sol);
    }
}
