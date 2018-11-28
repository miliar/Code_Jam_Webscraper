//
//  main.cpp
//  Fractiles
//
//  Created by Jake Sanders on 4/9/16.
//  Copyright © 2016 Jake Sanders. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

struct InputVals {
    int K_tiles;
    int C_complexity;
    int S_students;
};

int main(int argc, const char * argv[]) {
    std::ifstream input;
    input.open("input.txt");
    std::ofstream output;
    output.open("output.txt");
    
    if (input.is_open()) {
        int cases;
        input >> cases;
        
        std::vector<InputVals> foundArt (0);
        
        for (int a = 0; a < cases; a++) {
            int k;
            int c;
            int s;
            input >> k >> c >> s;
            InputVals InputInstance;
            InputInstance.K_tiles = k;
            InputInstance.C_complexity = c;
            InputInstance.S_students = s;
            foundArt.push_back(InputInstance);
        }
        
        for (int a = 0; a < cases; a++) {
            output << "Case #" << a + 1 << ": ";
            if (foundArt[a].K_tiles != foundArt[a].S_students) {
                output << "IMPOSSIBLE\n";
            } else {
                for (int b = 0; b < foundArt[a].S_students; b++) {
                    if (b == foundArt[a].S_students - 1)
                        output << b + 1 << "\n";
                    else
                        output << b + 1 << " ";
                }
            }
        }
    } else {
        std::cout << "Error\n";
    }
    return 0;
}
