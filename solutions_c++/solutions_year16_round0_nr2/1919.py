#include <iostream> 
#include <string>
#include "flip.hpp"

int main()
{
    int numberOfTestcases;
    std::string panstack;
    std::cin >> numberOfTestcases;
    for (int i = 1; i <= numberOfTestcases; i += 1) {
            std::cin >> panstack;
            std::cout << "Case #" << i << ": " << calculateMinNumberOfFlips(panstack) << "\n"; 
    }
}
