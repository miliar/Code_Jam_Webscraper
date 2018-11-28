//
//  main.cpp
//  Coin Jam
//
//  Created by Jake Sanders on 4/9/16.
//  Copyright © 2016 Jake Sanders. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <time.h>

unsigned long long convertBases(unsigned long long numToConvert, unsigned long long originalBase) {
    std::string numStr = std::to_string(numToConvert);
    unsigned long long num = 0;
    for (int place = 0; place < numStr.size(); place++) {
        num += (numStr[numStr.size() - place - 1] - 48) * (pow(originalBase,place));
    }
    return num;
}

//bool isPrime(unsigned long long num) {
//    for (unsigned long long divisor = 2; divisor <= num/2; divisor++) {
//        if (num % divisor == 0)
//            return false;
//    }
//    return true;
//}

unsigned long long getDivisor(unsigned long long num) {
    for (unsigned long long divisor = 2; divisor <= sqrt(num); divisor++) {
        if (num % divisor == 0)
            return divisor;
    }
    return 0; //If not prime
}

int main(int argc, const char * argv[]) {
    std::ifstream input;
    input.open("input.txt");
    std::ofstream output;
    output.open("output.txt");
    
    if (input.is_open()) {
        srand((int)time(nullptr));
        int one;
        int lengthOfNum;
        int numberOfNums;
        input >> one >> lengthOfNum >> numberOfNums;
        std::vector<std::vector<unsigned long long> > solutions (0);
        std::vector<unsigned long long> usedJams (0);
        while (solutions.size() != numberOfNums) {
            bool works = true;
            std::vector<unsigned long long> singleSolution (0);
            unsigned long long num = 0;
            for (int place = 0; place < lengthOfNum; place++) {
                if (place == 0)
                    num += (1 * pow(10,place));
                else if (place == lengthOfNum - 1)
                    num += (1 * pow(10,place));
                else {
                    int binaryDigit = rand() % 2;
                    num += (binaryDigit * pow(10,place));
                }
            }
            for (int a = 0; a < usedJams.size(); a++) {
                if (num == usedJams[a]) {
                    works = false;
                }
            }
            if (works) {
                singleSolution.push_back(num);
                for (int base = 2; base <= 10; base++) {
                    unsigned long long numInBase = convertBases(num, base);
                    unsigned long long divisor = getDivisor(numInBase);
                    if (divisor == 0) {
                        works = false;
                        break;
                    } else {
                        singleSolution.push_back(divisor);
                    }
                }
            }
            if (works) {
                solutions.push_back(singleSolution);
                usedJams.push_back(num);
                std::cout << "Solutions: " << solutions.size() << std::endl;
            }
        }
        output << "Case #1:\n";
        for (int a = 0; a < solutions.size(); a++) {
            for (int b = 0; b < solutions[a].size(); b++) {
                if (b == solutions[a].size() - 1)
                    output << solutions [a][b] << "\n";
                else
                    output << solutions[a][b] << " ";
            }
        }
    } else {
        std::cout << "Error\n";
    }
     /*
    int lengthOfNum = 16;
    int numberOfNums = 50;
    std::vector<unsigned long long> usedJams (0);
    while (true) {
        bool works = true;
        unsigned long long num = 0;
        for (int place = 0; place < lengthOfNum; place++) {
            if (place == 0)
                num += (1 * pow(10,place));
            else if (place == lengthOfNum - 1)
                num += (1 * pow(10,place));
            else {
                int binaryDigit = rand() % 2;
                num += (binaryDigit * pow(10,place));
            }
        }
        for (int a = 0; a < usedJams.size(); a++) {
            if (num == usedJams[a]) {
                works = false;
            }
        }
        if (works) {
            std::cout << num << std::endl;
            usedJams.push_back(num);
        }
    }*/
    return 0;
}