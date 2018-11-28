#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <vector>

void get_line(std::ifstream& infile, std::vector<double>& v) {
    std::string line;
    std::getline(infile, line);
    std::istringstream is(line);
    std::string token;
    while (std::getline(is, token, ' ')) {
        v.push_back(atof(token.c_str()));
    }
}

static const int PROD = 2;


double production(int fabrics, double productivity) {
    return fabrics * productivity + PROD;
}

int main(int argc, char* argv[]) {    
    std::ifstream infile(argv[1]);
    std::string line;
    std::getline(infile, line);
    int cases = atoi(line.c_str());
    std::cout.precision(15);
    for (int n = 0; n != cases; ++n) {
        std::vector<double> v;
        get_line(infile, v);

        double c = v[0];
        double f = v[1];
        double x = v[2];

        int fabrics = 0;
        double spend_time = 0;
        double time_to_done = 0;
        double next_time = 0;
        std::cout.precision(15);
        do {
            time_to_done = spend_time + x / production(fabrics, f);
            spend_time += c / production(fabrics, f);
            next_time = spend_time + x / production(++fabrics, f);
        } while(time_to_done > next_time);

        std::cout << "Case #" << n + 1 << ": " << time_to_done << "\n";
    }

    return 0;
}
