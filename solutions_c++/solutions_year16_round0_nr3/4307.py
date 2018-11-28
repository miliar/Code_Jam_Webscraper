//
//  main.cpp
//  Google Practice 1
//
//  Created by Ruowen Tan on 4/7/16.
//  Copyright (c) 2016 Ruowen Tan. All rights reserved.
//

#include <iostream>
#include <cassert>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

long get_decimal(long num, long base) {
    long factor = 1;
    long total = 0;
    
    while (num != 0) {
        total += (num % 10) * factor;
        num /= 10;
        factor *= base;
    }
    
    return total;
}

string get_binary(long num) {
    long base = 2;
    string result = "";
    string reverse = "";
    while (num != 0) {
        if (num % base == 1) {
            result = result + '1';
        } else {
            result = result + '0';
        }
        num /= 2;
    }
    
    for (size_t i = 0; i < result.size(); ++i) {
        reverse += result[result.size() - i - 1];
    }
    
    return reverse;
}

vector<string> get_all_cases(int length) {
    string min = "";
    string max = "";
    vector<string> result;
    min = min + '1';
    max = max + '1';
    for (size_t i = 0; i < length - 2; ++i) {
        min = min + '0';
        max = max + '1';
    }
    min = min + '1';
    max = max + '1';
    long min_case_bin = atol(min.c_str());
    long max_case_bin = atol(max.c_str());
    
    long min_case_dec = get_decimal(min_case_bin, 2);
    long max_case_dec = get_decimal(max_case_bin, 2);
    long a = min_case_dec;
    result.push_back(get_binary(a));
    
    for (size_t j = 0; j < (max_case_dec - min_case_dec) / 2; ++j) {
        result.push_back(get_binary(a + 2));
        a += 2;
    }
    return result;
    
}

struct Helper {
    bool not_prime;
    vector<long> vals;
};

void isPrime(long number, Helper & data, long & c){
    
    if(number < 2) {
        return;
    }
    if(number == 2) {
        return;
    }
    if(number % 2 == 0) {
        data.vals.push_back(2);
        c++;
        return;
    }
    for(long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) {
            data.vals.push_back(i);
            c++;
            return;
        }
    }
    return;
    
}





vector<Helper> determine_prime(vector<string> & data, int count) {
    bool not_prime;
    int not_primes = 0;
    long c;
    long value = 0;
    long j = 0;
    vector<Helper> result;
    while (not_primes < count + 1) {
        not_prime = false;
        c = long(0);
        Helper hh;
        for (long i = 2; i < 11; ++i) {
            value = get_decimal(atol(data[j].c_str()), i);
            //cout << value << endl;
            if (value < long(2)) {
                not_prime = false;
            } else {
                
                isPrime(value, hh, c);
                
            }
            if (c == long(9)) {
                not_prime = true;
            }
        }
        
        if (not_prime) {
            not_primes++;
            //cout << data[j] << " NOT PRIME" << endl;
        } else {
           // cout << data[j] << " PRIME\n" << endl;
        }
        j++;
        hh.not_prime = not_prime;
        result.push_back(hh);
        
    }
    return result;
}

int main(int argc, const char * argv[]) {
    
    
    FILE *fin = freopen("C-small.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("C-small.out", "w", stdout);
    int times;
    int counter = 0;
    int location = 0;
    int binary_length;
    int required_cases;
    vector<string> cases;
    vector<Helper> res;
    cin >> times;
    for (size_t i = 0; i < times; ++i) {
        cin >> binary_length;
        cin >> required_cases;
        
        cases = get_all_cases(binary_length);
        res = determine_prime(cases, required_cases);
        
        
        cout << "Case #" << (i + 1) << ": \n" ;
        while (counter < required_cases ) {
            if (res[location].not_prime) {
                cout << cases[location] << " ";
                
                for (size_t o = 0; o < res[location].vals.size(); ++o) {
                    cout << res[location].vals[o] << " ";
                }
                cout << "\n";
                counter++;
            }
            
            location++;
        }
        counter = 0;
        location = 0;
        
        
    }
    
    exit(0);
}
