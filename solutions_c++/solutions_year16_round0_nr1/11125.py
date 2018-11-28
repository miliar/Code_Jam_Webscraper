#include <iostream>
#include <fstream>
#include <sstream>

unsigned short checkForNumbers(unsigned long base);

int main(int argc, const char * argv[]) {
    std::ifstream inputFile;
    if(argc > 1) {
        inputFile.open(argv[1]);
        std::cin.rdbuf(inputFile.rdbuf());
    }
    
    int cases;
    unsigned short numsPending;
    unsigned long base;
    unsigned long solution;
    
    std::cin >> cases;
    
    for(int i = 0;i < cases;i++) {
        std::cin >> base;
        solution = base;
        numsPending = 0x03FF;
    
        do {
            unsigned short newCheck = checkForNumbers(solution);
            /*
            if(newCheck == numsPending) {
                std::cout << "Case #" << (i+1) << ": INSOMNIA\n";
                break;
            }*/
            if(base == 0) {
                std::cout << "Case #" << (i+1) << ": INSOMNIA\n";
                break;
            }
            
            numsPending = numsPending&newCheck;
            
            if(!numsPending) {
                std::cout << "Case #" << (i+1) << ": " << solution << "\n";
                break;
            }
            
            solution += base;
        }while (true);
    }
}

unsigned short checkForNumbers(unsigned long base) {
    unsigned short ret = 0x03FF;
    std::ostringstream oss;
    oss << base;
    
    const char * temp = oss.str().c_str();
    while(*temp) {
        unsigned char numberAgain = *temp - '0';
        ret = ret & ~(1 << numberAgain);
        temp++;
    }
    
    return ret;
}
