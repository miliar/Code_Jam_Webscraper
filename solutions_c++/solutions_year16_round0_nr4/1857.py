
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

#if 1
#define DBG
#else
#define DBG if (0) 
#endif

//================================================================================//

int g_numCases;
class TestCase {
public:
    int K;
    int C;
    int S;
};
std::list<TestCase> g_cases;

void parseInput(std::istream &is) {
    std::string str;
    // read number of cases
    is >> g_numCases;
    for (int i = 0; i < g_numCases; ++i) {
        TestCase c2;
        // add test case
        g_cases.push_back(c2);
        // back
        TestCase &c = g_cases.back();
        // read test case
        is >> c.K >> c.C >> c.S;
    }
}

#if 1
void createRandom() {
    /*std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> distrib(0, 1);*/

    int T = 1;
    for (int t = 0; t < T; ++t) {
        TestCase c2;
        g_cases.push_back(c2);
        TestCase &c = g_cases.back();
        c.K = 4;
        c.C = 100;
        c.S = 4;
    }
}
#endif

uint64_t powInt(uint64_t b, int p) {
    uint64_t r = 1;
    for (int i = 0; i < p; ++i) {
        r *= b;
    }
    return r;
}

int main() {
    printf("Problem D\n");
    //Utils::Timer timer;
    
#if 1
    //std::string inputFilename = "testInput.txt"; std::string outputFilename = "output-test.dat";
    std::string inputFilename = "D-small-attempt1.in"; std::string outputFilename = "output-small.dat";
    //std::string inputFilename = "B-large.in"; std::string outputFilename = "output-large.dat";

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

        int curNum = 0;

        DBG { std::cout << std::endl
                        << "K = " << c.K << ", C = " << c.C << ", S = " << c.S << std::endl; }
        
        if ((c.C == 1 && c.S < c.K) || (c.C > 1 && c.S < (c.K - 1))) {
            out << "Case #" << (nc + 1) << ": IMPOSSIBLE" << std::endl;
            DBG std::cout << "Case #" << (nc + 1) << ": IMPOSSIBLE" << std::endl;
        } else {
            out << "Case #" << (nc + 1) << ":";
            DBG std::cout << "Case #" << (nc + 1) << ":";
            
            if (c.C > 1) {
                int itop;
                if (c.S == c.K) {
                    itop = c.S - 1;
                    out << " " << 1;
                    DBG std::cout << " " << 1;
                } else {
                    itop = c.S;
                }
                
                //uint64_t b = powInt(c.K, c.C - 1) + 1;
                uint64_t b = c.K + 1;
                for (int i = 0; i < itop; ++i) {
                    uint64_t p = 1 + i * b + 1;
                    out << " " << p;
                    DBG std::cout << " " << p;
                }
                //uint64_t lastOne = powInt(c.K, c.C);
                //out << " " << lastOne;
                //DBG std::cout << " " << lastOne;
            } else {
                for (int i = 0; i < c.K; ++i) {
                    out << " " << (i + 1);
                    DBG std::cout << " " << (i + 1);
                }
            }
            
            out << std::endl;
            DBG std::cout << std::endl;
        }
        
        ++nc;
        //if (nc >= 5) exit(1);
    }

    printf("Done\n");
    //timer.check();
    //printf("Elapsed: %g sec\n", timer.getElapsed());
    return 0;
}

