#include <deque>
#include <iostream>

#include <cassert>
#include <cmath>

int main() {
    std::istream& in(std::cin);
    std::ostream& out(std::cout);
    int tests;
    in >> tests;
    
    #pragma omp parallel for ordered
    for (int test = 1; test <= tests; ++test) {
        int max;
        std::string chars;
        #pragma omp ordered
        in >> max >> chars;
        assert(chars.size() == max + 1);
        
        int standing = 0, friends = 0;
        for (int i = 0; i <= max; ++i) {
            int count = chars[i] - '0';
            int missing = std::max(0, i - standing);
            friends += missing;
            standing += count + missing;
        }
        
        #pragma omp ordered
        out << "Case #" << test << ": " << friends << std::endl;
    }
}
