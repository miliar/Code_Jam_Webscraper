/*
 *Created bv: Sai
 Created on: 11/4/15
 MY solution to the standing ovation problem presented in the qualification round for Google Code Jam 2015.
 * */

#include <iostream>
#include <cstdlib>


int main(int argc, char* argv[]){
    int t = 0;
    std::cin >> t;
    int numCase = 1;
    while(t--){
        int maxS = 0;
        std::string input;
        std::cin >> maxS;
        std::cin >> input;
        std::cin.ignore();

        std::string::iterator it = input.begin();
        int digit  = 0;
        int numPeople = 0;
        int addedPeople = 0;
        while(it != input.end()){
            if(digit > numPeople){
                addedPeople += digit - numPeople;
                numPeople += digit - numPeople;
            }
            int val = *it - '0';

            numPeople += val;

            it++;
            digit++;
        }
        std::cout << "Case #" << numCase << ": " << addedPeople << std::endl;
        numCase++;
    }


    return 0;   
}
