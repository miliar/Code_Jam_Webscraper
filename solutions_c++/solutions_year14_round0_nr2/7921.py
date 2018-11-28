#include <iostream>
#include <iomanip>

using namespace std;

double process(double farm_cost, double farm_capacity, double goal)
{
    double production_rate = 2.0;
    double total_time = 0;
    bool processing = true;
    
    while(processing) {
        double time_to_goal = goal / production_rate;      // tempo que levo com a produção atual
        double time_to_buy  = farm_cost / production_rate; // tempo para comprar uma nova fazenda
        double next_time_to_goal = time_to_buy + (goal / (production_rate + farm_capacity));
        
        if(time_to_goal > next_time_to_goal) {
            production_rate += farm_capacity;
            total_time += time_to_buy;
        }
        else {
            total_time += time_to_goal;
            processing = false;
        }
    }
    
    return total_time;
}

int main()
{
    unsigned int cases;
    
    cin >> cases;
    
    for(unsigned int k=1; k<=cases; k++)
    {
        double farm_capacity;
        double farm_cost;
        double goal;
        
        cin >> farm_cost >> farm_capacity >> goal;
        
        double time = process(farm_cost, farm_capacity, goal);
        
        cout << "Case #" << k << ": " << fixed << setprecision(7) << time << endl;
    }
    return 0;
}
