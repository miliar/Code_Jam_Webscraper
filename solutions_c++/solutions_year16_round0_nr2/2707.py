#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <ostream>
#include <string>
#include <deque>

std::ostream& operator<<(std::ostream& s, std::deque<bool> const& d) {
    s << "[";
    if(d.size() != 0) {
        s << (d[0] ? "true" : "false");
        for(std::deque<bool>::size_type i = 1 ; i < d.size() ; i++) {
            s << "," << (d[i] ? "true" : "false");
        }
    }
    return s << "]";
}

void flip_n(std::deque<bool>& test_case, std::deque<bool>::size_type n) {
    for(std::deque<bool>::size_type i = 0 ; i < n / 2 ; i++) {
        bool tmp = test_case[i];
        test_case[i] = !test_case[n - 1 - i];
        test_case[n - 1 - i] = !tmp;
    }

    if(n % 2 == 1) {
        test_case[n / 2] = !test_case[n / 2];
    }
}

void solve(std::deque<bool>& test_case) {
    unsigned int nb_flips = 0; // Number of flips required to get all +
    unsigned int total_pancakes = test_case.size(); // number of pancakes in the stack
    unsigned int last_minus = total_pancakes - 1; // position of the last - from the beginning
    while(!std::all_of(test_case.begin(), test_case.end(), [](bool b) { return b; })) {
        // We compute last_minus, so we know test_case[last_minus + 1]
        // to test_case[test_case.size() - 1] are correct
        for(unsigned int i = last_minus ; i != 0 ; i--) {
            if(test_case[i]) {
                last_minus--;
            } else {
                break;
            }
        }

        if(test_case[0]) {
            unsigned int to_flip = 1;
            for(unsigned int i = 1 ; i <= last_minus ; i++) {
                if(test_case[i])
                    to_flip++;
                else
                    break;
            }
            flip_n(test_case, to_flip);
            nb_flips++;
        } else {
            flip_n(test_case, last_minus + 1);
            nb_flips++;
        }
    }
    std::cout << nb_flips;
}

int main() {
    std::string line;
    unsigned int nb_cases;

    std::getline(std::cin, line);
    nb_cases = std::stoi(line, nullptr, 10);

    for(unsigned int i = 0 ; i < nb_cases ; i++) {
        std::deque<bool> test_case;
        std::getline(std::cin, line);
        test_case.resize(line.size(), false);

        for(std::string::size_type j = 0 ; j < line.size() ; j++) {
            if(line[j] == '+') {
                test_case[j] = true;
            }
        }

        std::cout << "Case #" << i + 1 << ": ";
        solve(test_case);
        std::cout << std::endl;
    }

    return EXIT_SUCCESS;
}

/*int main() {
    std::deque<bool> test_case = {true, false, false, false, true};
    std::cout << "Initial deque: " << test_case << std::endl;
    flip_n(test_case, 3);
    std::cout << "Flipping 3: " << test_case << std::endl;
    flip_n(test_case, 1);
    std::cout << "Flipping 1: " << test_case << std::endl;
    }*/
