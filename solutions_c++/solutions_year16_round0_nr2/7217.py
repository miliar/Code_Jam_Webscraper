#include <iostream>
#include <unordered_map>
#include <sstream>
#include <cstdint>
#include <vector>
#include <cassert>


bool allUnhappy(const std::vector<char>& pancakes){

    for(int i=0; i<pancakes.size(); ++i){
        if(pancakes[i] != '-'){
            return false;
        }
    }
    return true;


}
bool allHappy(const std::vector<char>& pancakes){

    for(int i=0; i<pancakes.size(); ++i){
        if(pancakes[i] != '+'){
            return false;
        }
    }
    return true;

}

int flipsNeeded(const std::string& original){
    int flips = 0;

    std::vector<char> pancakes;
    pancakes.reserve(100);

    for(int i=0; i<original.size(); ++i){
        assert(original[i] == '-' || original[i] == '+');
        pancakes.push_back(original[i]);
    }


    if(allHappy(pancakes))
        return flips;

    if(allUnhappy(pancakes)){
        flips++;
        return flips;
    }
    
    //std::cout << std::endl << std::string(pancakes.begin(), pancakes.end()) << std::endl;
    int plusIndex = 0;
    int i = 0;


    ///////////////////
    //go to next plus
    //flip all before it IF ANY
    //go to last connected plus
    //flip all after that plus inclusive
    //repeat
    //////////////////
    //
    //
    while(i<pancakes.size()){
        //find +
        if(pancakes[i] == '+'){

            //flip all before + if any
            if(i == 0){
                //do no flips
            }else{
                for(int j=0; j<i; ++j){
                    pancakes[j] = ((pancakes[j] == '-')? '+' : '-');
                }
                flips++;
            }

            if(allHappy(pancakes))
                return flips;

            //go to last adjacent + in group
            for(int p=i; p<pancakes.size(); ++p){
                if(pancakes[p] == '-'){
                    i = p-1;
                    break;
                    std::cout << i << " " << p << std::endl;
                }
            }

            //std::cout << std::string(pancakes.begin(), pancakes.end()) << std::endl;
            //flip everything up to and including +
            for(int k=0; k<=i; ++k){
                pancakes[k] = (pancakes[k] == '-')? '+' : '-';
            }

            flips++; //std::cout << std::string(pancakes.begin(), pancakes.end()) << std::endl;
            if(allHappy(pancakes))
                return flips;

        }

        if(i == pancakes.size() - 1){
            for(int k=0; k<pancakes.size(); ++k){
                if(pancakes[k] == '-'){
                    pancakes[k] = '+';
                }
            }
            flips++; //std::cout << std::string(pancakes.begin(), pancakes.end()) << std::endl;
            if(allHappy(pancakes))
                return flips;
        }

        i++;

    }

    return flips;
}


int main(){
    assert(flipsNeeded("-") == 1);
    assert(flipsNeeded("-+") == 1);
    assert(flipsNeeded("+-") == 2);
    assert(flipsNeeded("+++") == 0);
    assert(flipsNeeded("+++++++++++++++++") == 0);
    assert(flipsNeeded("-----------------") == 1);
    assert(flipsNeeded("--+-") == 3);
    assert(flipsNeeded("--+--+") == flipsNeeded("----+----+"));
    assert(flipsNeeded("-+-+") == flipsNeeded("---+---+"));

    assert(flipsNeeded("----+----+") == 3);
    assert(flipsNeeded("---+---+") == 3);

    assert(flipsNeeded("------------+") == 1);
    assert(flipsNeeded("-------------------------") == 1);
    assert(flipsNeeded("-+-+-+-+-+-+-+-+-+-+") == 19);
    assert(flipsNeeded("+-+-+-+-+-+-+-+-+-+") == 18);
    assert(flipsNeeded("+------------------") == 2);
    assert(flipsNeeded("--++") == 1);
    assert(flipsNeeded("+-++") == 2);
    assert(flipsNeeded("++-+") == 2);
    assert(flipsNeeded("++++------") == 2);

    int tests;
    std::cin >> tests;

    int current = 0;
    while(current++ < tests){
        std::string pancakeStr;
        std::cin >> pancakeStr;
        std::cout << "Case #" << current << ": " << flipsNeeded(pancakeStr) << std::endl;
    }




    return 0;
}
