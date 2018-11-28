
#include <iostream>
#include <unordered_map>
#include <sstream>
#include <cstdint>

std::string sleepCount(uint32_t N){
    std::unordered_map<char, bool> digitsFound;

    std::stringstream ss;


    uint32_t value;
    uint32_t i = 1;
    while(1){

        value = N * i;

        if(value<0 | N == 0)
            return "INSOMNIA";

        ss << value;
        std::string digits = ss.str();


        for(uint32_t j=0; j<digits.size(); ++j){
            digitsFound[digits[j]] = true;
        }
    

    
        if( digitsFound['0'] &&
            digitsFound['1'] &&
            digitsFound['2'] &&
            digitsFound['3'] &&
            digitsFound['4'] &&
            digitsFound['5'] &&
            digitsFound['6'] &&
            digitsFound['7'] &&
            digitsFound['8'] &&
            digitsFound['9']  ){
            
            return std::to_string(value);
        }
        else{
            i++;
        }
    }

}


int main(){
    int tests;
    std::cin >> tests;

    int current = 0;
    while(current++ < tests){
        int N;
        std::cin >> N;
        std::cout << "Case #" << current << ": " << sleepCount(N) << std::endl;
    }




return 0;
}
