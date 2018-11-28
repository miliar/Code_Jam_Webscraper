//
//  main.cpp
//  codejam
//
//  Created by Iulian Popescu on 09/04/16.
//  Copyright © 2016 Iulian Popescu. All rights reserved.
//

#include <fstream>
#include <vector>
#include <set>
#include <cmath>
using namespace std;

const string INPUT = "/Users/iulian_popescu/Documents/Code jam/codejam C - nok/codejam/input.in";
const string OUTPUT = "/Users/iulian_popescu/Documents/Code jam/codejam C - nok/codejam/output.in";

ifstream fin(INPUT);
ofstream fout(OUTPUT);

vector<int> jamcoin;
int jamcoinsFound = 0;

unsigned long long isPrime(unsigned long long number) {
    if (number != 2 && number % 2 == 0) {
        return 2;
    } else {
        for (unsigned long long i = 3; i <= sqrt(number); ++i) {
            if (number % i == 0) {
                return i;
            }
        }
    }
    return 1;
}

unsigned long long convertToBase(int base) {
    unsigned long long result = 0;
    int n = (int) jamcoin.size();
    for (int i = 0; i < n; i++) {
        result += pow(base, n - i -1) * jamcoin[i];
    }
    return result;
}

vector<unsigned long long> checkJamcoin() {
    vector<unsigned long long> divisors;
    for (int i = 2; i <= 10; ++i) {
        unsigned long long divisor = isPrime(convertToBase(i));
        if(divisor != 1) {
            divisors.push_back(divisor);
        } else {
            divisors.clear();
            return divisors;
        }
    }
    return divisors;
}

void genJamcoins(int i) {
    if(i == jamcoin.size() - 1) {
        vector<unsigned long long> result = checkJamcoin();
        if (result.size() == 9) {
            for (int index = 0; index < jamcoin.size(); ++index) {
                fout << jamcoin[index];
            }
            for (int index = 0; index < result.size(); ++index) {
                fout << " " << result[index];
            }
            fout << "\n";
            jamcoinsFound --;
            if (jamcoinsFound == 0) {
                exit(0);
            }
        }
    } else {
        jamcoin[i] = 1;
        genJamcoins(i+1);
        jamcoin[i] = 0;
        genJamcoins(i+1);
    }
}

void solve(int T) {
    int n = 0, j = 0;
    fin >> n >> j;
    jamcoinsFound = j;
    jamcoin.resize(n);
    jamcoin[0] = 1;
    jamcoin[n-1] = 1;
    fout << "Case #" << T << ":\n";
    genJamcoins(1);
}

int main(int argc, const char * argv[]) {
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
