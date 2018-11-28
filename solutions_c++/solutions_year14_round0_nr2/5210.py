#include<iostream>

using namespace std;
void bestStrategy(int);
int main()
{
    int testcases;
    cin >> testcases;
    int i;
    for (i = 1; i <= testcases; i++){
        bestStrategy(i);
    }
    return 0;
}

void bestStrategy(int i)
{
    long double cookies = 0.0;
    long double current_rate = 2.0;
    long double added_rate = 0.0;
    long double cost = 0.0;
    long double X = 0.0;
    cin >> cost >> added_rate >> X;

    long double time_to_buy_farm = 0.0;
    long double total_time_spent = 0.0;
    long double curr_best_time = 0.0;

    while (1) {
        curr_best_time = total_time_spent + X/current_rate;
        time_to_buy_farm = cost/current_rate;
        if (time_to_buy_farm + (X/(current_rate+added_rate)) + total_time_spent < curr_best_time) {
            current_rate += added_rate;
            total_time_spent += time_to_buy_farm;
        } else {
            std::cout.precision(7);
            std::cout << std::fixed;
            cout << "Case #" << i << ": " <<curr_best_time << endl;
            break;
        }
    }
}
