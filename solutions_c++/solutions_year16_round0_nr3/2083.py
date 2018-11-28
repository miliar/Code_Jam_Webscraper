#include <vector>
#include <iostream>
#include <cmath>
#include <limits>

template<typename ValType, typename PrimeType>
PrimeType getDivisor(ValType v, const std::vector<PrimeType>& primes) {
    ValType rt = sqrt(v);
    for(const auto p : primes) {
//       std::cout << "testing " << i << " vs " << p << "\n";
        if(p>rt) {
            return 0;
        }
        if(v%p==0) {
            return p;
        }
    }
    return 0;
}

std::vector<unsigned> genPrimes(size_t n) {
    std::vector<unsigned> v;
    v.reserve(n);
    v.push_back(2);
    for(unsigned i=3; v.size()<n; ++i) {
        if(getDivisor(i, v)==0) {
//            std::cout << i << " is prime\n";
            v.push_back(i);
        }
    }
    return v;
}

template<typename ValType>
__int128 convertBaseJamcoinLike(ValType bits, unsigned base) {
    __int128 v = 0;
    for(int i=sizeof(bits)*8-1; i>=0; --i) {
        v = v*base + ((bits >> i) & 1);
    }
    return v;
}

template<typename ValType>
std::string binToString(ValType bits) {
    std::string s;
    for(int i=sizeof(bits)*8-1; i>=0; --i) {
        unsigned v = ((bits >> i) & 1);
        if(v || !s.empty()) {
            s.push_back(v ? '1' : '0');
        }
    }
    return s;
}


int main() {
    int T;
    std::cin >> T;
    
    std::vector<unsigned> primes = genPrimes(1000);
//    for(const unsigned p : primes) {
//        std::cout << p << std::endl;
//    }

    for(size_t c=1; c<=T; ++c) {
        int N, J;
        std::cin >> N;
        std::cin >> J;
        std::cout << "Case #" << c << ":\n";
//std::cout << "N=" << N << " J=" << J << std::endl;
        const uint32_t first = (1LU << (N-1)) + 1LU;
        const uint32_t last = (1LLU << N) - 1LLU;
        
        for(uint32_t i=first, found=0; i!=last && found<J; i+=2) {
//std::cout << "Attempting " << binToString(i) << std::endl;
            std::vector<unsigned> divs;
            for(unsigned base=2; base<=10; ++base) {
                const auto v = convertBaseJamcoinLike(i, base);
                const auto div = getDivisor(v, primes);
                if(div) {
//std::cout << (unsigned long long)v << "b" << base << " has div " << div << std::endl;
                    divs.push_back(div);
                } else {
                    break;
                }
            }
            if(divs.size()==9) {
                ++found;
                std::cout << binToString(i);
                for(const auto d : divs) {
                    std::cout << " " << d;
                }
                std::cout << "\n";
            }
        }
    }

    return 0;
}


