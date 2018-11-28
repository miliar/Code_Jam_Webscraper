/** CyCraig33 - Google Code Jam 2016 Qualification Problem D **/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <unordered_map>
#include <iostream>

// 0 if prime
// otherwise first non-trivial factor
std::unordered_map<unsigned long long, unsigned long long> factors;

// We never have the case of 1 in a jam coin
unsigned long long checkPrimality(unsigned long long n) {
    unsigned long long bound = std::sqrt(n)+1;
    if( n == 2 ) return 0;
    //if( n%2 == 0 ) return 2;
    //for( int i = 3; i <= bound; i+=2 ) {
    //    if( n%i == 0 ) return i;
    //}
    if(n%3 == 0 ) return 3;
    if(n%5 == 0) return 5;
    if(n%7 == 0) return 7;
    return 0;
}

unsigned long long getFactor(unsigned long long n) {
    std::unordered_map<unsigned long long, unsigned long long>::const_iterator x;
    if((x = factors.find(n)) != factors.end()) {
        return x->second;
    } else {
        unsigned long long factor = checkPrimality(n);
        factors[n] = factor;
        return factor;
    }
}

unsigned long long convertBase(int base, bool* bits, int numBits) {
    unsigned long long N = 0;
    for(int i = 0; i < numBits; i++) {
        N += std::pow(base,numBits-i-1)*bits[i];
    }
    return N;
}

int numCoins, numBits, coinsNeeded;
unsigned long long currFactors[9];

void generateBitString(bool* bits, int currlen) {
    if( numCoins == coinsNeeded ) return;
    
    if( currlen == 0) {
        // first bit always 1
        bits[0] = 1;
        generateBitString(bits,currlen+1);
    } else if( currlen == numBits-1 ){
        // last bit always 1
        bits[numBits-1] = 1;
        generateBitString(bits,currlen+1);
    } else if( currlen < numBits ) {
        // generate next bit
        bits[currlen] = 0;
        generateBitString(bits,currlen+1);
        bits[currlen] = 1;
        generateBitString(bits,currlen+1);
    } else if( currlen == numBits ) {
        // check if jam coin
        for(int b = 2; b <= 10; b++) {
            unsigned long long N = convertBase(b, bits, numBits);
            unsigned long long factor = getFactor(N);
            //std::cout << factor << " is a factor of " << N << std::endl;
            if( factor > 1 ) {
                currFactors[b-2] = factor;
            } else {
                // prime => not a jam coin
                for(int i = 0; i < numBits; i++) {
                  //  printf("%d",bits[i]);
                }
                //printf(" is not a jam coin!\n");
                return;
            }
        }
        // not returned => jam coin
        for(int i = 0; i < numBits; i++) {
            printf("%d",bits[i]);
        }
        // print factors
        for(int i = 2; i <= 10; i++) {
            printf(" %d",currFactors[i-2]);
        }
        printf("\n");
        numCoins++;
        return;
    }
}

int main(void) {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("outsmall", "w", stdout);
    
    int numCases,caseNum = 0;
    scanf("%d",&numCases);
    while(numCases-- > 0) {
        numCoins = 0;
        scanf("%d %d",&numBits,&coinsNeeded);
        bool* bits = new bool[numBits];
        memset(bits,false,sizeof(bits));
        printf("Case #%d:\n",++caseNum);
        generateBitString(bits,0);
    }
    fflush(stdout);
    
    
    return 0;
}