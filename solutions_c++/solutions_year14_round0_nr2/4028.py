//dayka
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main() {

    ios_base::sync_with_stdio(0);

    int t, testcase;
    double base_velocity = 2;
    double c, f, x;
    bool ok;
    int number_of_farms;
    double best_result;
    double new_result;
    double velocity;

    cin >> t;

    for(testcase = 1 ; testcase <= t ; testcase++)
    {
        cin >> c >> f >> x;
        bool ok = true;
        int number_of_farms = 0;
        double best_result = 55000;
        double new_result = 55000;
        while(new_result <= best_result && ok)
        {
            double velocity = base_velocity;
            new_result = 0;
            int tmp_number_of_farms = number_of_farms;
            while(tmp_number_of_farms > 0 && new_result <= best_result)
            {
                new_result += c/velocity;
                velocity += f;
                tmp_number_of_farms--;
            }
            if(tmp_number_of_farms > 0)
                ok = false;
            new_result += x/velocity;
            if(new_result < best_result)
                best_result = new_result;
            number_of_farms++;
        }
        cout << "Case #" << testcase << ": ";
        cout << fixed;
        cout << setprecision(7) << best_result << endl;
    }

return 0;
}
