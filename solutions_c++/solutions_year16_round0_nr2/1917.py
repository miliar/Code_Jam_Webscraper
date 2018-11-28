
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
    std::vector<unsigned char> bits;
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
        is >> str;
        c.bits.resize(str.size());
        for (size_t j = 0; j < str.size(); ++j) {
            c.bits[j] = (str[j] == '-' ? 0 : 1);
        }
    }
}

#if 1
void createRandom() {
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> distrib(0, 1);

    int T = 100;
    for (int t = 0; t < T; ++t) {
        TestCase c2;
        g_cases.push_back(c2);
        TestCase &c = g_cases.back();
        c.bits.resize(100);
        for (int i = 0; i < 100; ++i) {
            c.bits[i] = distrib(rng);
        }
    }
}
#endif

bool areAllHappy(const std::vector<unsigned char> &bits) {
    for (size_t i = 0; i < bits.size(); ++i) {
        if (bits[i] == 0)
            return false;
    }
    return true;
}

void debugPrint(const std::vector<unsigned char> &bits) {
    static const char *digits = "-+";
    for (size_t i = 0; i < bits.size(); ++i) {
        printf("%c", digits[bits[i]]);
    }
    printf(" (%li)\n", bits.size());
}

void flip(std::vector<unsigned char> &bits, int num) {
    for (int i = 0; i < (num / 2); ++i) {
        unsigned char temp = bits[i];
        bits[i] = bits[num - 1 - i] ^ 1;
        bits[num - 1 - i] = temp ^ 1;
    }
    if ((num % 2) != 0) {
        bits[num / 2] ^= 1;
    }
    
    debugPrint(bits);
}

int main() {
    printf("Problem B\n");
    //Utils::Timer timer;
    
#if 1
    //std::string inputFilename = "testInput.txt"; std::string outputFilename = "output-test.dat";
    //std::string inputFilename = "B-small-attempt0.in"; std::string outputFilename = "output-small.dat";
    std::string inputFilename = "B-large.in"; std::string outputFilename = "output-large.dat";

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

        debugPrint(c.bits);
        int curNum = 0;
        while (1) {
            int j;
            for (j = (int) c.bits.size() - 1; j >= 0; --j) {
                if (c.bits[j] == 0) {
                    ++j;
                    break;
                }
            }
            printf("j = %i\n", j);
            if (j < 0) {
                //curNum = 0;
                break;
            } else {
                
                int k;
                for (k = 0; k < c.bits.size(); ++k) {
                    if (c.bits[k] == 0)
                        break;
                }
                if (k > 0) {
                    flip(c.bits, k);
                    ++curNum;
                }
                
                flip(c.bits, j);
                ++curNum;
            }
            
            //debugPrint(c.bits);
            //if (areAllHappy(c.bits))
            //    curNum = 0;
        }
        
        out << "Case #" << (nc + 1) << ": " << curNum << std::endl;
        DBG std::cout << "Case #" << (nc + 1) << ": " << curNum << "\n\n";
        
        ++nc;
        //if (nc >= 5) exit(1);
    }

    printf("Done\n");
    //timer.check();
    //printf("Elapsed: %g sec\n", timer.getElapsed());
    return 0;
}

