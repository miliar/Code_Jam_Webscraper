#include <sstream>
#include <fstream>
#include <string>

#include <algorithm>
#include <bitset>
#include <iostream>
#include <mutex>
#include <vector>

#include <thread>

#include <boost/multiprecision/cpp_int.hpp>



using namespace boost::multiprecision;

#define BITSET_LENGTH 32
//
//std::string intToBinaryString(int a,int length){
//    std::bitset<BITSET_LENGTH> x(a);
//    return x.to_string().substr( BITSET_LENGTH - length , length);
//}
//
//std::string nextCoin(){
//    static int middleLength = 1;
//    static int generatedCoinsWithCurrentMiddleLength = 0;
//
//    std::string returnString;
//
//    returnString = "1" + intToBinaryString(generatedCoinsWithCurrentMiddleLength, middleLength) + "1" ;
//    ++generatedCoinsWithCurrentMiddleLength;
//
//    if( generatedCoinsWithCurrentMiddleLength == ( 1 << middleLength ) ){
//        ++middleLength;
//        generatedCoinsWithCurrentMiddleLength = 0;
//    }
//    return returnString;
//}
 
void coinAnalyser();

std::mutex nextCoinMutex;

std::string nextCoin(){
    std::lock_guard<std::mutex> lock(nextCoinMutex);

    static int coin = (1 << (BITSET_LENGTH-1)) + 1;
    std::bitset<BITSET_LENGTH> x(coin);
    coin += 2 ; // leaves last digit as 1 
    return x.to_string();
}

int128_t findDivisor(int128_t number){
//    int128_t root = (int128_t)(std::sqrt(number));

    if(number % 2 == 0 ) return 2; // 2 is special case
    for(int128_t i = 3; i*i <= number ; i +=2){
        if(number % i == 0) return i;
    }
    return 1;
}

int128_t interpretInBaseN(std::string number, int base){
    int128_t returnValue;
    int128_t currentPositionValue = 1;

    for( auto it = number.rbegin() ; it != number.rend(); ++it){
        returnValue += ((int128_t)(*it)-'0') * currentPositionValue;
        currentPositionValue *= base;
    }
    return returnValue;
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

    std::thread t1(coinAnalyser);
    std::thread t2(coinAnalyser);
    std::thread t3(coinAnalyser);
    std::thread t4(coinAnalyser);
    std::thread t5(coinAnalyser);
    std::thread t6(coinAnalyser);
    std::thread t7(coinAnalyser);
    std::thread t8(coinAnalyser);

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();
    t6.join();
    t7.join();
    t8.join();

    return 0;
}

void coinAnalyser(){

    std::vector< std::vector<int128_t> > solutionVector(0);

    std::cerr << "started thread " << std::endl;
    int counter = 0;

    while(solutionVector.size() < 200){
        std::vector<int128_t> sol(0);
        
        std::string nextCoinCandidate = nextCoin();
        // pushback candidate in base10 for easy printing
        sol.push_back( interpretInBaseN(nextCoinCandidate, 10)); 

        if(++counter == 10){
            std::cerr << "at candidate " << nextCoinCandidate << std::endl;
            counter = 0;
        }

        for(int i=2; i <= 10; ++i){
            int128_t testNumber = interpretInBaseN(nextCoinCandidate, i);
            int128_t divisor = findDivisor(testNumber); 
            if(divisor == 1) break;
            else sol.push_back(divisor);
        }

        if(sol.size() == 10){
            solutionVector.push_back(sol);
            for(auto i : sol){
                std::cout << i << ' '; 
            }
            std::cout << std::endl;
        }
    }
}

