#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>   
#include <vector>
#include <string>

// clang++ A.cpp -o A -O3

// Run as ./A < input.txt

int main(int argc, const char *argv[]) {
    
    int T;
    std::string word;
    std::cin >> T;
	  	
    std::ofstream myfile;
    myfile.open ("output.txt");
    
    // Test cases
    for (int test = 0; test < T; test++) {
        
        // Read dimensions
        std::cin >> word;        
        
        std::string best;
        best += word[0];
        // Do stuff
        for(int i=1; i < word.size(); i++) {
            if(word[i] < best[0]) {
                best += word[i];
            }
            else {
                best = word[i] + best;
            }
        }
        
        // Print outcome
        myfile << "Case #" << (test + 1) << ": " << best << std::endl;
    }
}