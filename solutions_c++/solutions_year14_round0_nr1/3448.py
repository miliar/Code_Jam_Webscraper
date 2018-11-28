#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <iterator>
#include <vector>

std::set<int> get_row(std::ifstream& infile) {
    std::set<int> s;
    std::string line;
    std::getline(infile, line);
    int row = atoi(line.c_str());
    for (int l = 0; l != 4; ++l) {
        std::getline(infile, line);
        if (l == (row - 1)) {
            std::istringstream is(line);
            std::string token;
            while (std::getline(is, token, ' ')) {
                s.insert(atoi(token.c_str()));
            }
        }
    }
    return s;
}

typedef std::set<int>::const_iterator set_iter;

int main(int argc, char* argv[]) {    
    std::ifstream infile(argv[1]);
    std::string line;
    std::getline(infile, line);
    int cases = atoi(line.c_str());
    std::set<int> row1;
    std::set<int> row2;
    for (int n = 0; n != cases; ++n) {
        std::vector<int> result;
        row1 = get_row(infile);
        row2 = get_row(infile);

        for (set_iter it1 = row1.begin(); it1 != row1.end(); ++it1) {
            set_iter it2 = row2.find(*it1);
            if (it2 != row2.end()) {
                result.push_back(*it2);
            }
        }

        if (result.size() == 1) {
            std::cout << "Case #" << n + 1 << ": " << result[0] << "\n";
        } else if (result.size() == 0) {
            std::cout << "Case #" << n + 1 << ": Volunteer cheated!\n";
        } else {
            std::cout << "Case #" << n + 1 << ": Bad magician!\n";
        }
        
    }

    return 0;
}
