#include <sstream>
#include <fstream>
#include <string>

#include <algorithm>
#include <iostream>
#include <vector>


//flips stack from pVs begin until INCLUSIVE end
void flip(std::vector<int>& pVc, std::vector<int>::iterator end){
    for(auto it = pVc.begin(); it != end; ++it) *it = 1-*it;
    std::reverse(pVc.begin(), end);

    std::cerr << "Flipped " << end-pVc.begin() << " pancakes. Now it looks like : " ;
    for(auto i : pVc ) std::cerr << i ;
    std::cerr << std::endl;

}

bool existsZeroInPancake(const std::vector<int>&a){
    for(auto i : a) if( i == 0 ) return true;
    return false;
}

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
        std::istringstream iss(line);
        std::string pancakeInput(iss.str());

        std::vector<int> pDist(0);
//        pDist.reserve( pancakeInput.length());

        for(auto i : pancakeInput){
            if( i == '+' ) pDist.push_back(1);
            else if( i == '-' ) pDist.push_back(0);
            else std::cerr << "Readin error: got invalid value " << i << " in case " << case_ + 1 <<  std::endl;
            fgetc(stdin);
        }

        int basePancake = pDist.back();
        int totalFlips = 0;

        std::cerr << "Pancakes are ";
        for(auto i : pDist) std::cerr << i ;
        std::cerr << std::endl << "baseCake : " << basePancake << std::endl;
        
        while( existsZeroInPancake(pDist) ){
            if(*(pDist.begin()) == basePancake){
                std::cerr << "base == top" << std::endl;
                auto it = pDist.begin();
                while(*it == basePancake && it != pDist.end()) ++it;
                flip(pDist,it);
                ++totalFlips;
            }
            else{
                std::cerr << "base != top" << std::endl;
                auto it = pDist.end() - 1;
                while(*it == basePancake && it != pDist.begin()) --it;
                flip(pDist,++it); // need to go back one step
                ++totalFlips;
            }
        }

        std::cout << "Case #" << ++case_ <<  ": " << totalFlips <<std::endl;
        std::cerr << "-------------------------" << std::endl;

    }
    return 0;
}
