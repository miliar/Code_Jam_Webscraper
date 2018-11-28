#include <stdint.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>

typedef std::vector<int> VI;
typedef std::vector<bool> VB;
typedef std::vector<VI> VVI;
typedef std::pair<int, int> II;
typedef std::vector<II> VII;
typedef std::vector<VII> VVII;
typedef std::set<int> SI;
typedef std::list<int> LI;

int main() {
    int T;
    std::cin >> T;
    int C = 1;
    while(T--) {
        VI discs;
        int N, X;
        std::cin >> N >> X;
        for(int i = 0; i < N; i ++) {
            int v;
            std::cin >> v;
            discs.push_back(v);
        }
        std::sort(discs.begin(), discs.end());

        VB used(N, false);

        int c1 = 0;
        int c2 = N-1;
        int required = 0;


        while(c1 < N) {
            while(c1 < N && used[c1]) c1 ++;
            while(c2 >= 0 && used[c2]) c2 --;

            if(c1 >= N) break;
            if(c2 < 0) break;

            while(c2 >= 0 && (used[c2] || discs[c1] + discs[c2] > X)) c2 --;

            if(c2 < 0) break;

            used[c1] = true;
            used[c2] = true;
            required ++;
            c1 ++; c2 --;
        }

        while(c1 < N) {
            if(!used[c1]) required ++;

            c1 ++;
        }

        std::cout << "Case #" << C++ << ": " << required << std::endl;
    }
    return 0;
}
