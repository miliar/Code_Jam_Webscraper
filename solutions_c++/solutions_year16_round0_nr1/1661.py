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


    long long retVal = 0;
    long long N = 0;

    while (std::getline(infile, line))  // this does the checking!
    {
        std::istringstream iss(line);
        iss >> N;
        bool done = false;

        if(N == 0){
            std::cout << "Case #" << ++case_ <<  ": INSOMNIA"  << std::endl;
            continue;
        }
        std::vector<bool> seen(10);
        for(int a=0; a < seen.size() ; ++a){
            seen[a] = false;
        }
        // loop through numbers
        for(long long i = N; i < N*1000000 && !done; i+= N){
            std::string currentN = std::to_string(i);
            for(char j : currentN){
                seen[j-'0']  = true;
            }
            retVal = i;
            for(int a = 0 ; a < seen.size() && seen[a]  ; ++a){
                if(a == seen.size() -1 ) done = true;
            }
            if(i==N*99) std::cerr <<"possible problem ;) " << std::endl;
        }

        //for(int a=0; a<seen.size(); ++a) seen[a] = false;
        
        std::cout << "Case #" << ++case_ <<  ": " << retVal <<std::endl;

    }
    return 0;
}
