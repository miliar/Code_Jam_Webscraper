#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main(){
    freopen("t.in","r", stdin);
    freopen("t.out","w", stdout);
    int n;
    double cost_per_f, farm_r, goal;
    cin >> n;
    for (int test=1; test<=n; test++){
        cin >> cost_per_f >> farm_r >> goal;
        int current_f = 0;
        double tot = 0;
        while (true){
            double current_r = 2 + farm_r * current_f;
            double choice1 = goal/current_r;

            double time_for_one = cost_per_f / current_r;
            double future_r = current_r + farm_r;
            double choice2 = time_for_one + goal/future_r;

            if (choice1 <= choice2){
                tot += choice1;
                break;
            } else {
                tot += time_for_one;
                current_f += 1;
            }
        }
        cout << "Case #" << test << ": ";
        cout << setprecision(7) << fixed << tot << endl;
    }
}
