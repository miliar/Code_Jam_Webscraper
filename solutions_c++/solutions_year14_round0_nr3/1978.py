#include <iostream>
#include <stdint.h>
#include <cstdio>

uint32_t snoob(uint32_t x) {
   uint32_t smallest, ripple, ones;
                                // x = xxx0 1111 0000
   smallest = x & -x;           //     0000 0001 0000
   ripple = x + smallest;       //     xxx1 0000 0000
   ones = x ^ ripple;           //     0001 1111 0000
   ones = (ones >> 2)/smallest; //     0000 0000 0111
   return ripple | ones;        //     xxx1 0000 0111
}


int R, C;

int ind(int x, int y) {
    if(x < 0 || y < 0 || x >= R || y >= C) return -1;
    return x*C+y;
}

int count(uint32_t mask, int x, int y) {
    int c = 0;
    for(int xd = -1; xd <= 1; xd ++) {
        for(int yd = -1; yd <= 1; yd ++) {
            int in = ind(x+xd, y+yd);
            if(in == -1) continue;
            else if(mask & (1<<in)) c ++;
        }
    }
    return c;
}

uint32_t do_dfs(uint32_t mask, uint32_t mask2, int x, int y) {
    if(x < 0 || y < 0 || x >= R || y >= C) return mask2;
    if((1<<ind(x,y)) & mask) return mask2;

    //std::printf("index: %i\n", ind(x,y));
    mask2 |= (1<<ind(x,y));

    // don't spread if count nonzero
    if(count(mask, x, y) != 0) return mask2;

    for(int xd = -1; xd <= 1; xd ++) {
        for(int yd = -1; yd <= 1; yd ++) {
            int in = ind(x+xd,y+yd);
            if(in == -1) continue;

            // been here already?
            if(mask2 & (1<<in)) continue;
            if(mask & (1<<in)) continue;

            mask2 |= do_dfs(mask, mask2, x+xd, y+yd);
            /*
            if(count(mask, x+xd, y+yd) == 0) {
                //std::printf("moving from %i %i to %i %i\n", x, y, x+xd, y+yd);
                mask2 |= do_dfs(mask, mask2, x+xd, y+yd);
            }
            */

        }
    }

    return mask2;
}

int main() {
    int CA = 1;
    int T;
    std::cin >> T;
    while(T--) {
        std::cout << "Case #" << CA++ << ":" << std::endl;;

        int M;
        std::cin >> R >> C >> M;

        if(M == 0) {
            //std::cout << "XXX: possible" << std::endl;
            for(int i = 0; i < R; i ++) {
                for(int j = 0; j < C; j ++) {
                    if(i == 0 && j == 0) std::cout << "c";
                    else std::cout << ".";
                }
                std::cout << std::endl;
            }
            continue;
        }

        int max = R*C;
        uint32_t maxmask = 1<<max;
        uint32_t totalmask = (1<<max)-1;

        uint32_t sm = -1; int sr = -1; int sc = -1;

        uint32_t mask = (1<<M)-1;
        while((mask & maxmask) == 0 && sr == -1) {
            //std::printf("Trying mask 0x%x\n", mask);
            for(int r = 0; r < R; r ++) for(int c = 0; c < C; c ++) {
                //std::printf("\tTrying start position (%i,%i = %i)\n",
                    //r, c, ind(r,c));
                uint32_t result = do_dfs(mask, 0, r, c);
                //std::printf("\t\tresulting mask: 0x%x\n", result);
                //std::printf("\t\tresult vs total: %x/%x\n", (result | mask), totalmask);
                if((result | mask) == totalmask) {
                    sm = mask;
                    sr = r;
                    sc = c;
                    break;
                }
            }

            mask = snoob(mask);
        }

        if(sm == -1) std::cout << "Impossible" << std::endl;
        else {
            for(int r = 0; r < R; r ++) {
                for(int c = 0; c < C; c ++) {
                    if(r == sr && c == sc) std::cout << "c";
                    else if(sm & (1<<(ind(r,c)))) std::cout << "*";
                    else std::cout << ".";
                }
                std::cout << std::endl;
            }
        }
    }
    return 0;
}
