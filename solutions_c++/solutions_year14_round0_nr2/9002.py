//
//  main.cpp
//  cookie_clicker
//
//  Created by Vagelis Nonas on 4/12/14.
//
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>


double find_time(double C, double F, double X) {
    double cookies=0, cookies_per_sec=2.0, time_elapsed=0;
    while (1) {
        double time_to_make_cookies=(X-cookies)/cookies_per_sec;
        double time_to_buy_factory, time_left_if_buy_factory;
        if (cookies>C) {
            time_to_buy_factory=0;
            time_left_if_buy_factory=(X-(cookies-C))/(cookies_per_sec+F);
        } else {
            time_to_buy_factory=(C-cookies)/cookies_per_sec;
            time_left_if_buy_factory=X/(cookies_per_sec+F);
        }
        if (time_to_make_cookies<time_to_buy_factory+time_left_if_buy_factory) {
            return time_elapsed+time_to_make_cookies;
        } else {
            cookies_per_sec=cookies_per_sec+F;
            time_elapsed=time_elapsed+time_to_buy_factory;
        }
    }
}




int main(int argc, const char * argv[])
{
    try {
        int test_cases=0;
        std::cin >> test_cases;
        std::cout.precision(7);
        for (int i=0;i<test_cases;i++) {
            double C,F,X;
            std::cin >> C >> F >> X;
            std::cout << "Case #" << i+1 << ": " << std::fixed << std::showpoint << find_time(C,F,X) << std::endl;
        }
    } catch (const char * e) {
        std::cout << e;
    } catch (std::exception& e) {
        std::cout << e.what();
    }
}

