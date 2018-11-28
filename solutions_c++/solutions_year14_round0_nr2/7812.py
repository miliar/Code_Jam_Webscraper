#include <iostream>
#include <fstream>
#include <stdio.h>


double solve(double c, double f, double x) {
    double rate = 2.0;
    double new_rate = rate;
    double time = x/2.0;
    double new_time = time;
    double farm_time = 0.0;
    double add_farm = 0.0;

    do {
        rate = new_rate;
        time = new_time;
        farm_time += add_farm;
        
        add_farm = c/rate;
        new_rate = rate + f;
        double work_time = x/new_rate;
        new_time = add_farm + work_time + farm_time;

    } while(new_time < time);
    return time;

}



int main(int argc, char * argv[]) {

    std::fstream myfile(argv[1], std::ios_base::in);
    int num_cases;
    myfile >> num_cases;

    for(int i = 1; i <= num_cases; i++){
        double c, f, x;
        myfile >> c;
        myfile >> f;
        myfile >> x;
        double time = solve(c, f, x);
        printf("Case #%d: %.8f\n",i, time);
    }

}
