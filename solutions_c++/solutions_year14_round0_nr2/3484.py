//
//  main.cpp
//  CodeJam2014_CookieClicker
//
//  Created by Neurosion on 4/12/14.
//  Copyright (c) 2014 Neurosion Development. All rights reserved.
//

#include <fstream>

double calc_cookie_output(double farm_count, double cookie_count)
{
    return farm_count * cookie_count + 2.0;
}

double calc_next_farm_time(double cookie_output, double farm_cost)
{
    return farm_cost / cookie_output;
}

double cookies_in_time(double cookie_output, double seconds)
{
    return cookie_output * seconds;
}

int main(int argc, const char * argv[])
{
    std::ifstream input("/Users/neurosion/Documents/Projects/CodeJam2014_CookieClicker/B-large.in");
    std::ofstream output("/Users/neurosion/Documents/Projects/CodeJam2014_CookieClicker/output-large-2.dat");
    output.precision(7);
    output.setf( std::ios::fixed, std:: ios::floatfield );

    int test_cases;
    input >> test_cases;
    
    for (int i = 1; i <= test_cases; ++i) {
        double farm_cost, cookie_output, goal;
        input >> farm_cost;
        input >> cookie_output;
        input >> goal;
        static char buffer[1024];
        input.getline(buffer, 1024);
        
        bool done = false;
        double farm_count = 0.0;
        double elapsed = 0.0;
        do {
            double current_output = calc_cookie_output(farm_count, cookie_output);
            double time_to_complete_current = goal / current_output;
            
            double next_output = calc_cookie_output(farm_count + 1, cookie_output);
            double next_farm_time = calc_next_farm_time(current_output, farm_cost);
            double time_to_complete_next = next_farm_time + goal / next_output;
            
            if (time_to_complete_current < time_to_complete_next) {
                elapsed += time_to_complete_current;
                done = true;
            }
            else {
                elapsed += next_farm_time;
                farm_count += 1.0;
            }
        } while (!done);
        
        output << "Case #" << i << ": " << elapsed << "\n";
    }
    
    input.close();
    output.close();
    
    return 0;
}

