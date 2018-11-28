#include <iostream>
#include <stdint.h>
#include <cstdio>

uint64_t best(int N, uint64_t w) {
    uint64_t total = 1<<N;
    uint64_t needed = 1;
    uint64_t left = total-w-1;
    uint64_t bits = 0;

    while(needed <= left) {
        left -= needed;
        needed *= 2;
        bits ++;
    }

    uint64_t pos = 0;

    uint64_t p = 1ULL<<(N-1);

    for(; bits > 0; bits --, p >>=1) {
        pos += p;
    }
    
    return total-pos-1;
}

uint64_t worst(int N, uint64_t w) {
    if(w == 0) return 0;

    uint64_t needed = 1;
    uint64_t left = w;
    uint64_t bits = 0;

    while(needed <= left) {
        left -= needed;
        needed *= 2;
        bits ++;
    }

    uint64_t pos = 0;

    uint64_t p = 1ULL<<(N-1);

    for(; bits > 0; bits --, p >>=1) {
        pos += p;
    }
    
    return pos;
}

uint64_t find_p(uint64_t N, uint64_t P, uint64_t w, uint64_t s) {
    uint64_t b = best(N, w);
    //std::printf("find_g(%lu, %lu, %lu, %lu)\n", N, P, w, s);
    //std::printf("\tw = %lu, b = %lu\n", w, b);
    if(s == 0 && b < P) return w;
    else if(s == 0 && b >= P) return w-1;
    if(b < P) return find_p(N, P, w+s, s/2);
    else return find_p(N, P, w-s, s/2);
}


uint64_t find_p(uint64_t N, uint64_t P) {
    return find_p(N, P, 1<<(N-1), 1<<(N-2));
}

uint64_t find_g(uint64_t N, uint64_t P, uint64_t w, uint64_t s) {
    uint64_t b = worst(N, w);
    //std::printf("find_g(%lu, %lu, %lu, %lu)\n", N, P, w, s);
    //std::printf("\tw = %lu, b = %lu\n", w, b);
    if(s == 0 && b < P) return w;
    else if(s == 0 && b >= P) return w-1;
    if(b < P) return find_g(N, P, w+s, s/2);
    else return find_g(N, P, w-s, s/2);
}

uint64_t find_g(uint64_t N, uint64_t P) {
    return find_g(N, P, 1<<(N-1), 1<<(N-2));
}

int main() {
    int T;
    std::cin >> T;
    for(int C = 1; C <= T; C ++) {
        uint64_t N, P;
        std::cin >> N >> P;
        if(P == (1<<N)) {
            std::printf("Case #%i: %lu %lu\n", C, (1<<N)-1, (1<<N)-1);
            continue;
        }
        if(N == 1) {
            std::printf("Case #%i: %lu %lu\n", C, 0, 0);
            continue;
        }

        uint64_t g = find_g(N, P);
        uint64_t p = find_p(N, P);

        std::printf("Case #%i: %lu %lu\n", C, g, p);
    }
    return 0;
}
