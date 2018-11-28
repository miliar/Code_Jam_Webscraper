
// NOTE: for the big-dataset version, I'm using the gmp library (libgmp + libgmpxx)

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
#include <gmpxx.h>
//#include "/usr/scratch/bartezza/bar-boe/mzlUtils/mzlUtils/Timer.h"
//#include "/Users/bartezza/Documents/bar-boe/mzlUtils/mzlUtils/Timer.h"
//#include "Geometry.h"
//#include "Strings.h"
//#include "Utils.h"
//#include "Numbers.h"

#if 0
uint64_t g_table16[][16] = {
//#include "table-16.h"
{ 1ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL, 0ULL },
{ 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL, 1ULL },
{ 1ULL, 2ULL, 4ULL, 8ULL, 16ULL, 32ULL, 64ULL, 128ULL, 256ULL, 512ULL, 1024ULL, 2048ULL, 4096ULL, 8192ULL, 16384ULL, 32768ULL },
{ 1ULL, 3ULL, 9ULL, 27ULL, 81ULL, 243ULL, 729ULL, 2187ULL, 6561ULL, 19683ULL, 59049ULL, 177147ULL, 531441ULL, 1594323ULL, 4782969ULL, 14348907ULL },
{ 1ULL, 4ULL, 16ULL, 64ULL, 256ULL, 1024ULL, 4096ULL, 16384ULL, 65536ULL, 262144ULL, 1048576ULL, 4194304ULL, 16777216ULL, 67108864ULL, 268435456ULL, 1073741824ULL },
{ 1ULL, 5ULL, 25ULL, 125ULL, 625ULL, 3125ULL, 15625ULL, 78125ULL, 390625ULL, 1953125ULL, 9765625ULL, 48828125ULL, 244140625ULL, 1220703125ULL, 6103515625ULL, 30517578125ULL },
{ 1ULL, 6ULL, 36ULL, 216ULL, 1296ULL, 7776ULL, 46656ULL, 279936ULL, 1679616ULL, 10077696ULL, 60466176ULL, 362797056ULL, 2176782336ULL, 13060694016ULL, 78364164096ULL, 470184984576ULL },
{ 1ULL, 7ULL, 49ULL, 343ULL, 2401ULL, 16807ULL, 117649ULL, 823543ULL, 5764801ULL, 40353607ULL, 282475249ULL, 1977326743ULL, 13841287201ULL, 96889010407ULL, 678223072849ULL, 4747561509943ULL },
{ 1ULL, 8ULL, 64ULL, 512ULL, 4096ULL, 32768ULL, 262144ULL, 2097152ULL, 16777216ULL, 134217728ULL, 1073741824ULL, 8589934592ULL, 68719476736ULL, 549755813888ULL, 4398046511104ULL, 35184372088832ULL },
{ 1ULL, 9ULL, 81ULL, 729ULL, 6561ULL, 59049ULL, 531441ULL, 4782969ULL, 43046721ULL, 387420489ULL, 3486784401ULL, 31381059609ULL, 282429536481ULL, 2541865828329ULL, 22876792454961ULL, 205891132094649ULL },
{ 1ULL, 10ULL, 100ULL, 1000ULL, 10000ULL, 100000ULL, 1000000ULL, 10000000ULL, 100000000ULL, 1000000000ULL, 10000000000ULL, 100000000000ULL, 1000000000000ULL, 10000000000000ULL, 100000000000000ULL, 1000000000000000ULL },
};
#endif

/*uint64_t g_table32[][32] = {
#include "table-32.h"
};*/

#if 0
#define DBG
#else
#define DBG if (0) 
#endif

//================================================================================//

int g_numCases;
class TestCase {
public:
    int N;
    int J;
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
        is >> c.N >> c.J;
    }
}

#if 0
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

typedef std::vector<int> JamCoin;

typedef mpz_class BigInt;
//typedef uint64_t BigInt;

typedef unsigned int DivInt;
//typedef uint64_t DivInt;

BigInt g_table[11][32];

void createTable() {
    for (int b = 2; b <= 10; ++b) {
        g_table[b][0] = 1;
        for (int p = 1; p < 32; ++p) {
            g_table[b][p] = g_table[b][p - 1] * b;
        }
    }
}

void increase(JamCoin &c) {
    int i = 0;
    do {
        ++i;
        c[i] ^= 1;
    } while (c[i] == 0);
}

BigInt convertToNumber(const JamCoin &c, int base) {
    BigInt n = 0;
    for (int i = 0; i < (int) c.size(); ++i) {
        n += g_table[base][i] * c[i];
    }
    return n;
}

DivInt findDivisor(const BigInt &num) {
    if (num <= 3)
        return 0;
    if ((num % 2) == 0)
        return 2;
    if ((num % 3) == 0)
        return 3;

#if 0
    BigInt divMax = (BigInt) floor(std::sqrt(num));
    //BigInt divMax = num - 1;
    //uin64_t divMax = 
    if (divMax >= 1000000)
        divMax = 1000000;
#else
    DivInt divMax = 1000000;
#endif
    
    for (DivInt i = 5; i <= divMax; i += 6) {
        if ((num % i) == 0)
            return i;
        if ((num % (i + 2)) == 0)
            return i + 2;
    }
    return 0;
}

int main() {
    printf("Problem C\n");
    //Utils::Timer timer;

    createTable();
    
    //printf("%llu\n", (0xFFFFFFFFFFFFFFFF));
    //exit(1);
    
#if 1
    //std::string inputFilename = "testInput.txt"; std::string outputFilename = "output-test.dat";
    //std::string inputFilename = "C-small-attempt1.in"; std::string outputFilename = "output-small.dat";
    std::string inputFilename = "C-large.in"; std::string outputFilename = "output-large.dat";

    std::ifstream file(inputFilename);
    if (!file) {
        printf("[ERROR] Could not open '%s'\n", inputFilename.c_str());
        exit(1);
    }
    parseInput(file);
    file.close();
    printf("Input file '%s' parsed, %i cases\n", inputFilename.c_str(), g_numCases);
#elif 0
    std::string outputFilename = "output-custom.dat";
    createCustom();
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
    for (auto cas: g_cases) {
    #if 0
        int N = 32;
        int J = 500;
    #elif 0
        int N = 16;
        int J = 50;
    #else
        int N = cas.N;
        int J = cas.J;
    #endif
        
        int numCoins = 0;
        
        JamCoin c;
        //c[0] = 1; c[1] = 1; c[2] = 0; c[3] = 0; c[4] = 0; c[5] = 1;
        c.assign(N, 0);
        c[0] = 1;
        c[c.size() - 1] = 1;
        
        std::vector<DivInt> divs(10);
        
        out << "Case #" << (nc + 1) << ":\n";
        DBG std::cout << "Case #" << (nc + 1) << ":\n";
        
        while (1) {
            BigInt numBase10 = convertToNumber(c, 10);
            //printf("Checking %llu\n", numBase10);
        
            bool notCoin = false;
            for (int b = 2; b <= 10; ++b) {
                BigInt num = convertToNumber(c, b);
                
                DivInt div = findDivisor(num);
                if (div == 0) {
                    notCoin = true;
                    break;
                }
                divs[b] = div;
                
                //printf("%i) %llu\n", b, num);
                DBG std::cout << b << " " << num << " " << div << "\n";
            }
            if (notCoin == false) {
                ++numCoins;
                printf("Found (%i)!\n", numCoins);
                
                //if (numCoins == 2) exit(1);

                out << numBase10;
                for (int b = 2; b <= 10; ++b) {
                    out << " " << divs[b];
                }
                out << std::endl;
                
                DBG { std::cout << numBase10;
                for (int b = 2; b <= 10; ++b) {
                    std::cout << " " << divs[b];
                }
                std::cout << std::endl; }
                
                if (numCoins == J)
                    break;
            }
            
            increase(c);
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

