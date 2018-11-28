#include <iostream>
#include <cmath>

int main() {
    // Represents the number of test cases
    int testCount;
    
    // Reads in the number of test cases
    std::cin >> testCount;
        
    // Performs each trial
    for (int test = 1; test <= testCount; ++test) {
        // Reads test specifications
        long long k, c, s;
        std::cin >> k >> c >> s;
        
        // Precalculates the offset
        long long offset = pow(k, c - 1);
        
        // Displays trial
        std::cout << "Case #" << test << ":";
        
        for (long long i = 0; i < k; ++i) {
            std::cout << " " << 1 + offset * i;
        }
        
        std::cout << std::endl;
    }
    
    return 0;
}
