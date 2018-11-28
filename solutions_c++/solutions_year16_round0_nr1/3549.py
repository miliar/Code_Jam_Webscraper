#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <vector>

int func(int init_v){
    std::vector<bool> digits(10,false);
    if(init_v == 0){
        return -1;
    }


    for(int n = 1; n < 100000; ++n){
        int v = init_v * n;
        std::string s = std::to_string(v);
        //std::cout << s.size() << std::endl;
        for(int i = 0; i < s.size(); ++i){
            //std::cout << int(s[i]) - int('0') << std::endl;
            digits[int(s[i])-int('0')] = true;
        }

        bool res = true;
        for(auto d: digits){
            res = res & d;
        }
        if(res){
            return v;
        }
    }

    return -1;
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
        int v = std::atoi(line.c_str());

        int res = func(v);
        std::cout << v << std::endl;
        if(res >= 0){
            std::cout << "Case #" << i+1 <<": " << res << std::endl;
            out_file  << "Case #" << i+1 <<": " << res << std::endl;
        }else{
            std::cout << "Case #" << i+1 <<": INSOMNIA" << std::endl;
            out_file  << "Case #" << i+1 <<": INSOMNIA" << std::endl;
        }
    }

    return 0;
}
