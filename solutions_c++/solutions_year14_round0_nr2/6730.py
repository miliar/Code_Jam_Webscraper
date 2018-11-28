#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n_cases = 0;
    cin >> n_cases;
    cout << fixed;
    cout.precision(9);
    for (int kz = 1; kz <= n_cases; ++kz) {
        double farm_cost = 0.0, farm_rate = 0.0, objective = 0.0;
        cin >> farm_cost >> farm_rate >> objective;
        //cout << farm_cost << " " << farm_rate << " " << objective << endl;

        const double base_rate = 2.0;
        double t_to_N_farms = 0.0;
        double cur_rate = base_rate;
        double min_t_for_obj = objective / cur_rate;

        for (int NF = 1; NF < INT_MAX; ++NF) {
            t_to_N_farms += farm_cost / (base_rate + (NF - 1) * farm_rate);
            //cout << "t_to_N_farms: " << t_to_N_farms << endl;

            double cur_t_for_obj = t_to_N_farms + objective / (base_rate + NF * farm_rate);
            //cout << "cur_t_for_obj: " << cur_t_for_obj << endl;
            if (cur_t_for_obj < min_t_for_obj) {
                min_t_for_obj = cur_t_for_obj;
            } else {
                break;
            }
        }

        cout << "Case #" << kz << ": " << min_t_for_obj << endl;

    }
    return 0;
}