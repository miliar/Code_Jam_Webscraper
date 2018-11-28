#include <iostream>
#include <cstdint>
#include <string>

using namespace std;

int main()
{
    std::uint16_t nbTestCase; 
    std::cin >> nbTestCase;
    
    for (std::uint16_t i = 0; i < nbTestCase; i++) {
        std::uint64_t nbStanding = 0;
        std::uint16_t nbFriends = 0;
        
        std::uint16_t maxShynessLevel;
        std::string audience;
        std::cin >> maxShynessLevel;
        std::cin >> audience;
        
        for (std::uint16_t j = 0; j < audience.size(); j++) {
            std::uint16_t nbAtThatLevel = std::uint16_t(audience[j] - '0');
            
            if (nbStanding <= j && audience[j] == '0') {
                nbFriends++;            
                nbStanding += 1;
            }
            
            nbStanding += nbAtThatLevel;
        }
        
        std::cout << "Case #" << (i + 1) << ": " << nbFriends << std::endl;
    }
    
    return 0;
}

