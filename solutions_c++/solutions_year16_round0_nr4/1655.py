#include <sstream>
#include <fstream>
#include <string>

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char**argv){

    if(argc != 2){
        std::cout << "Pass the filename" << std::endl;
        return 0;
    }

    std::string line;
    std::ifstream infile(argv[1]);

    int case_ = 0;
    std::getline(infile,line); // discard number of cases

 
    while (std::getline(infile, line))  // this does the checking!
    {
        std::vector<int> solutionVector(0);
        std::istringstream iss(line);
        int K = 0, // length of tile sequence
            C = 0, // complexity of seq
            S = 0; // number of tiles to look at
        
        iss >> K ; iss >> C ; iss >> S;

        for(int i=1 ; i <= S ; ++i){
            solutionVector.push_back(i);
        }

        std::cout << "Case #" << ++case_ <<  ":" ;
        for(auto i : solutionVector) std::cout << ' '  << i;
        std::cout << std::endl;

    }
    return 0;
}
