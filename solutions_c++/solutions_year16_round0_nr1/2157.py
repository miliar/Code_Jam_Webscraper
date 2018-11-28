#include<iostream>
#include<bitset>
#include<cmath>



void test(unsigned long const N){
    std::bitset<10> has = std::bitset<10>(0);
    if ( N == 0 ){
        std::cout << "INSOMNIA";
        return;
    }
    unsigned long n = 0;
    long p = 0;
    while(!has.all()){
        n += N;
        p = 0;
        while(std::pow(10, p) <= n){
            unsigned long m = n / std::pow(10, p);
            has[m % 10] = true;
            p+=1;
        }
    }
    std::cout << n;
}


int main(){
    int test_limit = 0;
    std::cin >> test_limit;
    for(int i=0;i<test_limit;++i){
        unsigned long N;
        std::cin >> N;
        std::cout << "Case #" << i + 1 << ": ";
        test(N);
        std::cout << std::endl;
    }
}
