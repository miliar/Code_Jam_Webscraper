#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <vector>
#include <algorithm>


int solve(std::string stack){
    int flips(0);
    for(int i = 0; i < stack.size()-1; ++i){
        if(stack[i]!=stack[i+1]){
            ++flips;
        }
    }
    return flips + (stack[stack.size()-1]=='+'?0:1);
}

int main(int argc, char *argv[]){

    std::string line;
    std::ifstream in_file (argv[1]);
    std::ofstream out_file (argv[2]);

    int num_test_cases;
    getline(in_file,line);
    num_test_cases = std::atoi(line.c_str());

    std::cout << "#cases: " << num_test_cases << std::endl;

    for(int i = 0; i < num_test_cases; ++i){
        getline(in_file,line);
        int res = solve(line);
        std::cout << "Case #" << i+1 <<": " << res << std::endl;
        out_file  << "Case #" << i+1 <<": " << res << std::endl;
    }

    return 0;
}
