//
//  main.cpp
//  StandingOvation
//
//  Created by Chris Welhoelter on 4/10/15.
//  Copyright (c) 2015 Chris Welhoelter. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

int main(int argc, const char * argv[]) {
    
    std::string fileName;
   
    std::cout << "file name: ";
    std::cin >> fileName;
    std::cout << std::endl;
    
    std::fstream fs;
    fs.open(fileName);
    
    if (!fs.is_open()){
        std::cout << "couldn't open file" << std::endl;
        exit(EXIT_FAILURE);
    }
    
    int testCases;
    
    fs >> testCases;
    
    for (size_t i = 0; i < testCases; i++){
        
        int shynessBound;
        int peopleStanding = 0;
        int additionalPeople = 0;
        std::string rounds;
        
        fs >> shynessBound;
        fs >> rounds;
        
        for (size_t j = 0; j <= shynessBound; j++){
            
            int nextRound = rounds[j] - '0';

            if (peopleStanding < j && nextRound != 0){
                additionalPeople += j-peopleStanding;
                nextRound += j-peopleStanding;
            }
            
            peopleStanding += nextRound;
        }
        
        std::cout << "Case #" << i + 1 << ": " << additionalPeople << std::endl;
    }
    
    return 0;
}
