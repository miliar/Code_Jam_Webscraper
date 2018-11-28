//
//  main.cpp
//  Google Code Jam
//
//  Created by xiaoxin ren on 4/8/16.
//  Copyright © 2016 xiaoxin ren. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <bitset>
#include <gmp.h> // Added dymanic library.
// #include <gdbm.h>
using namespace std;
const string FILENAME = "small";


// Get primes less than 10000.
vector<int> primeArray() {
    vector<bool> nums(10001, true);
    vector<int> primes;
    for (int i = 2; i < 10000; i++) {
        if (nums[i]) {
            primes.push_back(i);
            int j = i*i;
            while (j <10000) {nums[j] = false; j += i;}
        }
    }
    
    return primes;
    
}

int main() {
    // insert code here...
    ifstream fin (FILENAME+ ".in");
    ofstream fout (FILENAME + ".out");
    int n, j;
    fin >> n >> n >> j;
    fin.close();
    vector<int> primes = primeArray();

    
    srand(time(NULL));
    
    fout << "Case #1:\n";
    mpz_t integ;
    mpz_init(integ);
    unsigned long resid = 0;
    string s;
    int i = 2;
    
    while (j){
        string val = ('1' + bitset<30>(rand()>>1).to_string() + '1');
        s = string(val);
        i = 2;
        for (; i < 11; i++) {
            // cout << "Not changed " <<val << '\n';
            int valid = mpz_set_str(integ, val.c_str(), i);
            if (valid < 0) {
                cout << "Not Valid\n";
                exit(EXIT_FAILURE);
            }
            // cout <<valid << ' ' << i<< ' '<< mpz_get_str(NULL, 10, integ)<<'\n';
            for (int prime: primes) {
                resid = mpz_fdiv_ui(integ, prime);
                // cout << prime << ' '<< resid << '\n';
                if (!resid) {
                    s += ' '+to_string(prime);
                    break;
                }
            }
            if (resid) break;
        }
        if (i == 11) { fout << s  << '\n'; j--;}
    }
    
    fout.close();
    
    
    return 0;
}
