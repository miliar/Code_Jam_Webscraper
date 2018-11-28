//
//  main.cpp
//  A
//
//  Google Code Jam 2k15 - Round 0 - Problem A
//

#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    int cases, current;
    int smax;
    std::string instr;
    
    std::cin >> cases;
    for (current=1; current<=cases; ++current) {
        int up = 0, extras = 0;
        int p;
        std::cin >> smax;
        std::cin >> instr;
        
        for (int s=0; s<=smax; ++s) {
            p = instr[s] - '0';
            if (s > up) {
                extras += s - up;
                up += s - up;
            }
            up += p;
        }
        
        std::cout << "Case #" << current << ": ";
        std::cout << extras << std::endl;
    }
}

