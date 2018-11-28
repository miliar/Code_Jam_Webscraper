//compile with boost library
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

uint128_t MAX_DIV = 100;

uint128_t toBase(uint128_t n, int base){
    uint128_t res = 0, e = 1;
    while(n){
        res += (n & 1) * e;
        e *= base;
        n >>= 1;
    }
    return res;
}

uint128_t findDiv(uint128_t n){
    for(uint128_t i=3; i<MAX_DIV; i+=2){
        if(n % i == 0)
            return i;
    }
    return 0;
}

void comp(int tc){
    int N, J;
    cin >> N >> J;
    
    cout << "Case #" << tc << ":" << endl;
    uint128_t one = 1;
    uint128_t cur = (one << (N-1)) | one;
    vector<uint128_t> divs;
    divs.reserve(9);
    while(J){
        bool ok = true;
        divs.clear();
        uint128_t converted = 0;
        for(int b=2; ok && b<=10; ++b){
            converted = toBase(cur, b);
            uint128_t div = findDiv(converted);
            if(div == 0){
                ok = false;
            }else{
                divs.push_back(div);
            }
        }
        
        if(ok){
            J--;
            cout << converted;
            for(auto d : divs){
                cout << " " << d;
            }
            cout << endl;
        }
        
        cur += 2;
    }
}

int main(){
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i){
        comp(i);
    }
}