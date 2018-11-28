
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cassert>
#include <random>
//#include "/usr/scratch/bartezza/bar-boe/mzlUtils/mzlUtils/Timer.h"
//#include "/Users/bartezza/Documents/bar-boe/mzlUtils/mzlUtils/Timer.h"
//#include "Geometry.h"
//#include "Strings.h"
//#include "Utils.h"
//#include "Numbers.h"

int getNumDigitsBase2(int x) {
    return x ? 32 - __builtin_clz(x) : 0;
}

int g_tenToThe[] = {
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
};

int getNumDigitsBase10(int x) {
    int guess[33] = {
        0, 0, 0, 0, 1, 1, 1, 2, 2, 2,
        3, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        6, 6, 6, 6, 7, 7, 7, 8, 8, 8,
        9, 9, 9
    };
    int digits = guess[getNumDigitsBase2(x)];
    return digits + (x >= g_tenToThe[digits]);
}

inline int getDigit(int x, int i) {
    return (x / g_tenToThe[i]) % 10;
}

#if 1
#define DBG
#else
#define DBG if (0) 
#endif

//================================================================================//

int g_numCases;
class TestCase {
public:
    int num;
};
std::list<TestCase> g_cases;

void parseInput(std::istream &is) {
    // read number of cases
    is >> g_numCases;
    for (int i = 0; i < g_numCases; ++i) {
        TestCase c2;
        // add test case
        g_cases.push_back(c2);
        // back
        TestCase &c = g_cases.back();
        // read test case
        is >> c.num;
    }
}

void createRandom() {
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> distrib(0, 1000000);

    int T = 100;
    for (int t = 0; t < T; ++t) {
        TestCase c2;
        g_cases.push_back(c2);
        TestCase &c = g_cases.back();
        c.num = distrib(rng);
    }
}

int main() {
    printf("Problem A\n");
    //Utils::Timer timer;
    
#if 1
    //std::string inputFilename = "testInput.txt"; std::string outputFilename = "output-test.dat";
    //std::string inputFilename = "A-small-attempt0.in"; std::string outputFilename = "output-small.dat";
    std::string inputFilename = "A-large.in"; std::string outputFilename = "output-large.dat";

    std::ifstream file(inputFilename);
    if (!file) {
        printf("[ERROR] Could not open '%s'\n", inputFilename.c_str());
        exit(1);
    }
    parseInput(file);
    file.close();
    printf("Input file '%s' parsed, %i cases\n", inputFilename.c_str(), g_numCases);
#else
    std::string outputFilename = "output-random.dat";
    createRandom();
#endif

    std::ofstream out(outputFilename);
    if (!out) {
        printf("[ERROR] Could not open '%s' for output\n", outputFilename.c_str());
        exit(1);
    }

    int nc = 0;
    for (auto c: g_cases) {
        int ans = 0;
        
        int curNum = c.num;
        // check
        if (curNum != 0) {
            unsigned short digitsSeen = 0;
            int i;
            while (1) {
                // count digits
                int numDigits = getNumDigitsBase10(curNum);
                for (int j = 0; j < numDigits; j++) {
                    int digit = getDigit(curNum, j);
                    digitsSeen |= 1 << digit;
                }
                // check
                if (digitsSeen == 1023)
                    break;
                // advance
                curNum += c.num;
            }
            out << "Case #" << (nc + 1) << ": " << curNum << std::endl;
            DBG std::cout << "Case #" << (nc + 1) << ": " << curNum << std::endl;
        } else {
            out << "Case #" << (nc + 1) << ": INSOMNIA" << std::endl;
            DBG std::cout << "Case #" << (nc + 1) << ": INSOMNIA" << std::endl;
        }
        
        ++nc;        
        //if (nc >= 5) exit(1);
    }

    printf("Done\n");
    //timer.check();
    //printf("Elapsed: %g sec\n", timer.getElapsed());
    return 0;
}

