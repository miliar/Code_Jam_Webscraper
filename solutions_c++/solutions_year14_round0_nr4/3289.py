#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <algorithm>

void get_line(std::ifstream& infile, std::vector<double>& v) {
    std::string line;
    std::getline(infile, line);
    std::istringstream is(line);
    std::string token;
    while (std::getline(is, token, ' ')) {
        v.push_back(atof(token.c_str()));
    }
}

typedef std::vector<double> masses;
typedef masses::iterator mass_iter;

int deceitful(masses naomi, masses ken) {
    int count = 0;
    size_t size = naomi.size();
    for (size_t i = 0; i < size; ++i) {
        if (*(naomi.end() - 1) > *(ken.end() - 1)) {
            ++count;
            naomi.erase(naomi.end() - 1);
            ken.erase(ken.end() - 1);
        } else {
            naomi.erase(naomi.begin());
            ken.erase(ken.end() - 1);
        }
    }
    return count;
}

int true_war(masses naomi, masses ken) {
    int count = 0;
    mass_iter rem = ken.end();
    for (size_t i = 0; i < naomi.size(); ++i ) {
        rem = ken.end();
        for (mass_iter it = ken.begin(); it != ken.end(); ++it) {
            if (*it > naomi[i]) {
                rem = it;
                break;
            }
        }
        if (rem != ken.end()) {
            ken.erase(rem);
        } else {
            ken.erase(ken.begin());
            ++count;
        }
    }
    return count;
}

int main(int argc, char* argv[]) {    
    std::ifstream infile(argv[1]);
    std::string line;
    std::getline(infile, line);
    int cases = atoi(line.c_str());
    std::cout.precision(15);
    for (int n = 0; n != cases; ++n) {
        std::getline(infile, line);
        int blocks = atoi(line.c_str());
        std::vector<double> naomi;
        get_line(infile, naomi);
        std::vector<double> ken;
        get_line(infile, ken);

        std::sort(naomi.begin(), naomi.end());
        std::sort(ken.begin(), ken.end());

        int dec = deceitful(naomi, ken);
        int war = true_war(naomi, ken);

        std::cout << "Case #" << n + 1 << ": " << dec << " " << war<< "\n";
    }

    return 0;
}
