#include <cstdio>
#include <iostream>

using namespace std;

int main(){
    //freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i){
        double min_time = 1e9, farm, add, win;
        cin >> farm >> add >> win;

        for (int fin_farms = 0; fin_farms <= 5000; ++fin_farms){
            double cur_time = 0, cur_farming = 2.0;
            for (int cur_farm = 0; cur_farm < fin_farms; ++cur_farm){
                cur_time += (farm / cur_farming);
                cur_farming += add;
            }
            cur_time += win / cur_farming;
            min_time = min(min_time, cur_time);
        }
        cout.precision(20);
        cout << "Case #" << i + 1 << ": " << min_time << "\n";
    }
}
