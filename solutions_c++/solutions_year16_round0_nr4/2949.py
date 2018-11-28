#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stdint.h>

// a bit crappy :P
void solveRec(std::vector<bool>& checked, std::vector<uint64_t> positions, int c, int complexity, int num_tiles, int students, bool& done, std::vector<uint64_t>& solution){
    if(c < complexity){
        bool flag = false;
        for(int i = 0; i < num_tiles; ++i){
            if(!checked[i]){
                flag = true;
                checked[i] = true;
                positions[c] = i;
                solveRec(checked,positions,c+1,complexity,num_tiles,students,done,solution);
            }
        }
        if(!flag){
            positions[c] = 0;
            solveRec(checked,positions,c+1,complexity,num_tiles,students,done,solution);
        }
    }else{
        if(solution.size() >= students){
            return;
        }
        uint64_t id = 1;
        for(int i = 0; i < positions.size(); ++i){
            std::cout << " " << positions[i];
            //if(num_tiles > complexity){
                uint64_t p = 1;
                for(int j = 0; j < positions.size()-1-i; ++j){
                    p *= num_tiles;
                }
                //std::cout << "p"<<p<<std::endl;
                //id += std::pow(num_tiles,positions.size()-1-i)*(positions[i]);
                id += p*positions[i];
                //std::cout << "id"<<id<<std::endl;
            //}else{
              //  id += std::pow(num_tiles,i)*(positions[i]);
            //}

        }
        std::cout << "("<< id <<")";
        std::cout << std::endl;

        solution.push_back(id);
        done = true;
        for(int i = 0; i < checked.size() && done; ++i){
            done &= checked[i];
        }
    }

}

int main(int argc, char *argv[]){

    std::ifstream in_file (argv[1]);
    std::ofstream out_file (argv[2]);

    int num_test_cases = 0;
    in_file >> num_test_cases;

    for(int i = 0; i < num_test_cases; ++i){
        int num_tiles,complexity,num_students;
        in_file >> num_tiles;
        in_file >> complexity;
        in_file >> num_students;

        std::vector<bool> checked(num_tiles,false);
        std::vector<uint64_t> positions(complexity,0);
        std::vector<uint64_t> solution;

        std::cout << "Case #" << i+1 << ":";
        out_file << "Case #" << i+1 << ":";

        bool done = false;
        solveRec(checked,positions,0,complexity,num_tiles,num_students, done, solution);
        std::cout << "-------------" << std::endl;
        if(!done){
            std::cout << " IMPOSSIBLE";
            out_file << " IMPOSSIBLE";
        }else{
            for(auto v: solution){
                std::cout << " " << v;
                out_file << " " << v;
            }
        }

        std::cout << std::endl;
        out_file << std::endl;
    }


    return 0;
}
