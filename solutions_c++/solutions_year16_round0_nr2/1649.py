#include <iostream>
#include <string>

int main() {
    // Represents the number of test cases
    int testCount;
    
    // Reads in the number of test cases
    std::cin >> testCount;
    
    // Performs each trial
    for (int test = 1; test <= testCount; ++test) {
        // Reads in pile
        std::string pile;
        std::cin >> pile;
        
        // Initializes number of flips and starting symbol for that many flips
        int flips = 0;
        char side = '+';
        
        for (int pancake = pile.size() - 1; pancake >= 0; --pancake) {
            if (side != pile[pancake]) {
                ++flips;
                side = pile[pancake];
            }
        }
        
        std::cout << "Case #" << test << ": " << flips << std::endl;
    }
}