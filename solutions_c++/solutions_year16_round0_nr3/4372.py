#include <bits/stdc++.h>
#include <cstdint>

#define forn(i,n) for(int i = 0; i < n; i++)

using namespace std;

uint64_t nbaseb(string bits, int base){
    uint64_t n = 0;
    int blen = bits.length();
    for(int i = 0; i < blen; i++){
        n += (bits[i] - '0') * pow(base, blen-i-1);
    }
    return n;
}

void generateNext(string& current){

    int clen = current.length();
    int i = clen-2;

    if(current[i] == '0') current[i] = '1';
    else {
        do {
            current[i] = '0';
            i--;
        } while(current[i] == '1' and i > 0);
    }

    current[i] = '1';
}

bool isNotPrime(uint64_t n, uint64_t& divisor){
    uint64_t sqrtn = sqrt(n);
    for(uint64_t i = 2; i <= sqrtn; i++){
        if(n % i == 0){
            divisor = i;
            return true;
        }
    }
    return false;
}

int main(){

    int testCases;
    uint64_t divisor, divisors[11];
    int n, j, counter;
    string input;

    cin >> testCases;
    forn(tt, testCases){

        cin >> n >> j;
        cout << "Case #" << tt + 1 << ":" << endl;

        counter = 0;

        // generates input bit sequence
        input = "1";
        for(int i = 0; i < n-2; i++) input += '0';
        input += '1';

        
        while(counter < j){

            for(int i = 2; i <= 10; i++){

                if(isNotPrime(nbaseb(input, i), divisor)){
                    divisors[i] = divisor;
                }
                else break;

                if(i == 10){
                    cout << input;
                    for(int k = 2; k <= 10; k++) cout << " " << divisors[k];
                    cout << endl;
                    counter++;
                }
                

            }

            generateNext(input);
            
        }
    }

    return 0;
}