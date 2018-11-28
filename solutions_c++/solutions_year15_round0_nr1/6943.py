
#include <iostream>
#include <string>

int main() {
    
    int num = 0;
    std::cin >> num;
    
    for ( int i = 0; i < num; ++i ) {
        
        int shy;
        std::cin >> shy;

        std::string levelInt;
        std::cin >> levelInt;

        int helpers = 0;
        int standingUp = 0;
        for ( int shyLevel = 0; shyLevel <= shy; ++shyLevel ) {
            int amountOfShyPeople = (levelInt[shyLevel] - '0');
            if ( shyLevel > standingUp+helpers ) {
                helpers += shyLevel - (standingUp+helpers);
            }
            standingUp += amountOfShyPeople;
        }

        std::cout << "Case #" << (i+1) << ": " << helpers << std::endl;
    }
    
    return 0;
}

