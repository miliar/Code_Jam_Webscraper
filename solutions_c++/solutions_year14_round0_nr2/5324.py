#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <iomanip> 
using namespace std;

int main(){
    int total_cases;
    cin >> total_cases;
    cout << std::setprecision(7);
    for(int cur_case = 1; cur_case <= total_cases ; cur_case++ )
    {
        double cost, extra, goal;
        cin >> cost >> extra >> goal;
        double perpare_time = 0;
        double start_speed = 2.;
        double time = goal / start_speed;
        while(true)
        {
            perpare_time += cost / start_speed;
            start_speed += extra;
            double new_time = perpare_time + goal / start_speed;
            if(new_time > time)
            {
                cout << "Case #" << cur_case << ": ";
                cout << time << "\n";
                break;
            }
            time = new_time;
        }
    }
    return 0;
}
