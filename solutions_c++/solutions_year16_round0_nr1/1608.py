#include <iostream>

int main() {
    // Represents the number of test cases
    int testCount;
    
    // Reads in the number of test cases
    std::cin >> testCount;
    
    // Performs each trial
    for (int test = 0; test < testCount; ++test) {
        // Represents each possible digit as an array of bools
        bool digits[10];
        
        // Initializes the starting value
        int n;
        std::cin >> n;
        
        // Stores the current value
        int pos = n;
        
        // Prints the current test
        std::cout << "Case #" << (test + 1) << ": ";
        
        // Hard coded case for 0, which will never introduce new digits...
        if (n == 0) {
            std::cout << "INSOMNIA" << std::endl;
            continue;
        }
        
        // Initializes all digits to false
        for (int i = 0; i < 10; ++i) {
            digits[i] = false;
        }
        
        // Represents if all digits are found
        bool allFound = false;
        
        // Performs algorithm to try each iN, until all digits are found
        while (!allFound) {
            // Copies N for intermediate calculations
            int tempN = pos;
            
            // Iterates through each digit of N
            while (tempN != 0) {
                digits[tempN % 10] = true;
                tempN = tempN / 10;
            }
            
            // Checks to see if all digits have been found
            allFound = true;
            
            for (int digit = 0; digit < 10; ++digit) {
                if (!digits[digit]) {
                    allFound = false;
                    break;
                }
            }
            
            // Increases position
            pos += n;
        }
        
        // As the position increases in each iteration, it is n too large
        std::cout << (pos - n) << std::endl;
    }
}