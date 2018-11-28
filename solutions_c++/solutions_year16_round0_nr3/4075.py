#include <iostream>
#include <bitset>

using namespace std;

int divisor(unsigned long long n){
    for(int i=2;i<n;i++){
        if(n%i==0) return i;
    }
    return 1;
}

bool isPrime(unsigned long long n){
    for(int i=2;i<500000&&i<n;i++){
        if(n%i==0) return false;
    }
    return true;
}

unsigned long long interpret(unsigned int coin, unsigned int base){
    unsigned long long n=0,b=1;
    for(int i=0;coin!=0;i++){
        if(1&coin){
            n+=b;
        }
        coin>>=1;
        b*=base;
    }
    return n;
}

bool isCoin(unsigned long long coin){
    for(int base=2;base<=10;base++){
        if(isPrime(interpret(coin,base))) return false;
    }
    return true;
}

int main(void){
    int T,N,J;
    cin >> T >> N >> J;
    cout << "Case #1:" << endl;
    int coin=1<<(N-1); coin++;
    for(int i=1;i<=J;i++){
        while(true){
            if(isCoin(coin)){
                if(N==16)cout << static_cast<bitset<16> >(coin);
                if(N==32)cout << static_cast<bitset<32> >(coin);
                for(int base=2;base<=10;base++){
                    cout << ' ' << divisor(interpret(coin,base));
                }
                cout << endl;
                coin+=2;
                break;
            }else{
                coin+=2;
                continue;
            }
        }
    }
    return 0;
}