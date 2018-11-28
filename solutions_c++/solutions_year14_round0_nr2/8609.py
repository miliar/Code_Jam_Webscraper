#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;
string line;
int numCases = 0;

double target_t(int farms, double bonus, double target) {
    double time = target / ((farms * bonus) + 2.0);
    return time;
}

double x_t(double farm_cost, double bonus_per_farm, double target) {
    bool done = false;
    int farms = 0;
    double total_time = 0.0;
    
    
    while(!done) {
        // time until next farm possible
        double farm_time = target_t(farms,bonus_per_farm,farm_cost);
        // continue without buying a farm
        double x_time = target_t(farms,bonus_per_farm,(target - farm_cost));
        // spend cookies on a farm
        double x_time_w_farm = target_t((farms + 1), bonus_per_farm, target);

        if(x_time > x_time_w_farm) {
            total_time += farm_time;
            farms++;
        } else {
            total_time = total_time + x_time + farm_time;
            done = true;
        }
    }

    return total_time;
}

int main() {
    getline(cin,line);
    stringstream (line) >> numCases;
    cout.precision(8);

    for(int i = 1; i <= numCases; i++) {
        double farm_cost, bonus_per_farm, target;
        int farms = 0;
        getline(cin,line);
        stringstream (line) >> farm_cost >> bonus_per_farm >> target;
        
        cout << fixed;
        cout << "Case #" << i << ": " << x_t(farm_cost,bonus_per_farm,target) << endl; 
    }
    return 0;
}
