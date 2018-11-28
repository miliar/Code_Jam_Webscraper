#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <primesieve.hpp>

#define DIGITS 16

using namespace std;

typedef long long ll;

std::vector<int> primes;
ll coins[11];
ll counter;

/* This function calculates (ab)%c */
int modulo(int a,int b,int c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}

bool Fermat(ll p,int iterations){
    if(p == 1){ // 1 isn't prime
        return false;
    }
    for(int i=0;i<iterations;i++){
        // choose a random integer between 1 and p-1 ( inclusive )
        long long a = rand()%(p-1)+1; 
        // modulo is the function we developed above for modular exponentiation.
        if(modulo(a,p-1,p) != 1){ 
            return false; /* p is definitely composite */
        }
    }
    return true; /* p is probably prime */
}

ll convertNumber(string number, int base) {
    ll converted = 0;
    int i = 0;
    while(i < DIGITS) {
        converted += (number[DIGITS-1-i]-'0')*pow(base, i);
        i++;
    }
    return converted;
}

bool isJamcoin(string number) {
    int base = 2;
    while(base <= 10) {
        ll converted = convertNumber(number, base);
        // cout << "in base " << base << " number " << converted << " is "; 
        if(Fermat(converted, 1000)) {
            // cout << "prime" << endl;
            return false;
        } else {
            coins[base] = converted;
            // cout << "not prime" << endl;
        }

        base++;
    }

    return true;
}

void increment(string &number) {
    int len = number.length() - 1;
    while(len >= 0) {
        if(number[len] == '1') {
            number[len] = '0';
            len--;
            continue;
        } else {
            number[len] = '1';
            break;
        }
    }
}

ll getDivisor(ll number) {
    vector<int>::iterator it = primes.begin();
    while(it != primes.end()) {
        if(number%(*it) == 0) {
            return *it;
        }
        it++;
    }

    // if(number%2 == 0) {
    //     return 2;
    // }

    // ll x = 3;
    // while(x < number) {
    //     if(number%x == 0) {
    //         return x;
    //     }
    //     x += 2;
    // }
    // cout << "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" << endl;
    return 0;
}

void printAnswer(string number) {
    ll divisors[11];

    int i = 2;
    while(i <= 10) {
        // cout << coins[i] << "-";
        divisors[i] = getDivisor(coins[i]);
        if(divisors[i] == 0) {
            counter--;
            return;
        }
        i++;
    }
    
    cout << number << " ";
    i = 2;
    while(i <= 10) {
        cout << divisors[i] << " ";
        i++;
    }
    cout << endl;
}

int main() {
    ll T, N, J, i, k;
    primesieve::generate_primes(100000000, &primes);
    
    cout << "Case #1:\n";
    counter = 0;
    string number = "1000000000000001";
    while(counter < 50) {

        if((number[0] == '1') && (number[DIGITS-1] == '1')) {
            if(isJamcoin(number)) {
                printAnswer(number);
                counter++;
            }
        }

        increment(number);
    }

    return 0;
}