#include <iostream>
bool digits[10];
int total;

void countDigits(int v){
    int n = v;
    while(n != 0){
        if(! digits[n%10]){
            digits[n%10] = true;
            ++total;
        }
        n /= 10;
    }
    
}

int main(){
    
    int T;
    int N;
    
    std::cin >> T;
    
    for(int i = 1; i <= T; ++i){
        total = 0;
        for(int i = 0; i < 10; ++i) digits[i] = false;
        std::cin >> N;
        int initialN = N;
        if(N == 0) total = 22;
        int j = 1;
        while(total < 10) {
            countDigits(N);
            ++j;
            if(total < 10) N=initialN*j;
        }
        if(total < 22) std::cout << "Case #"<<i<<": " << N << std::endl;
        else std::cout <<"Case #"<<i<<": " << "INSOMNIA" << std::endl;
    }
}