#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double CookieGen(double cookies, double time, double building, double C, double F, double X)
{
    double make_cookies = X/(2.0+building*F), build_time = C/(2.0+building*F), build_cookies = X/(2.0+(building+1.0)*F);
    // If make cookies is longer than create a building and make cookies
    while(make_cookies>build_time+build_cookies)
    {
        // The time spent is the time previously spent + the time to make one more building
        time += build_time;
        // We count this new building we just create
        building++;
        // The new timing to make cookies
        make_cookies = build_cookies;
        // The new timing to create one more building
        build_time = C/(2.0+building*F);
        // The new timing to make cookies with one more building
        build_cookies = X/(2.0+(building+1.0)*F);
    }
    // The time spent after making all buildings to make all cookies we need
    return time+make_cookies;
}

int main(int argc, char *argv[])
{
    ifstream file_input("B-large.in", ios::in);
    ofstream file_output("B-large(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        int games, test=1;
        double C, F, X;
        file_input >> games;
        while(test<=games)
        {
            file_input >> C >> F >> X;

            file_output << "Case #" << test << ": ";

            file_output << fixed << setprecision(7) << CookieGen(0.0,0.0,0.0,C,F,X) << "\n";
            test++;
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file !" << endl;
    return 0;
}
