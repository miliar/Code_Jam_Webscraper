#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

ofstream outfile("Cout.out");

bool is_prime(long long n, long long &proof) {
    if( n <= 1){ 
        return false;
    } else if( n <= 3) {
        return true;
    } else if(  n % 2 == 0 ){
        proof = 2;
        return false;
    } else if( n % 3 == 0 ){
        proof = 3;
        return false;
    }
    long long i = 5;
    while( i * i <= n ){
        if( n % i == 0 ){
            proof = i;
            return false;
        }
        if( n % (i+2) == 0 ){
            proof = i+2;
            return false;
        }
        
        i += 6;
    }
    return true;
}

void next( vector<int> &digits ){
    for( int i = 1 ; i < digits.size() ; ++i ){
        if( digits[i] == 0 ) {
            digits[i] = 1;
            break;
        }
        digits[i] = 0;
    }
}

long long convert(vector<int> digits, int base ){
    long long mult = 1;
    long long number = 0;
    for( int i = 0 ; i < digits.size() ; ++i ){
        number += digits[i] * mult;
        mult *= base;
    }
    
    return number;
}
   
string tostring( vector<int> digits ){
    ostringstream stream;

    for( int i = digits.size() - 1 ; i >= 0 ; --i ){
        stream<<digits[i];
    }
    
    return stream.str();
}

int main(){
    vector<int> digits;
    int array[] = {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};
    digits.assign( array, array+16);
    int J = 0;
    
    outfile<<"Case #: 1"<<endl;
    while( J < 50 ){
        next(digits);
        bool succes = true;
        vector<long long> proofs;
        
        for( int base = 2 ; base <= 10 ; ++base ){
            long long number = convert(digits, base);
            long long proof = 0;
            
            bool prime = is_prime(number, proof);
            
            if( prime ) {
                succes = false;
                break;
            }
            proofs.push_back(proof);
        }
        
        if( !succes ) continue;
        J++;
        
        outfile<<tostring(digits)<<" ";
        for( int i= 0 ; i < proofs.size() ; ++i ){
            outfile<<" "<<proofs[i];
        }
        outfile<<endl;
    }
    return 0;
}
