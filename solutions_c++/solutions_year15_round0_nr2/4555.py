#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<int> VI;
typedef std::vector<VI> VVI;

int DP[1001][1001] = {
#include "B.h"
};
int completed = 0;

int dp(int a, int b) {
    if(a == 0) return 0;
    if(DP[a][b] != 0) return DP[a][b];
    if(b == 0) {DP[a][b] = a; return a;}

    // starting case: we need at most as many turns as with b-1 movements
    DP[a][b] = dp(a, b-1);

    // try all splitting points
    for(int i = 1; i < a; i ++) {
        int p1 = i;
        int p2 = a-i;
        //std::cout << "p1: " << p1 << " p2: " << p2 << std::endl;
        for(int j = 0; j <= b-1; j ++) {
            DP[a][b] = std::min(DP[a][b], std::max(dp(p1, j), dp(p2, b-1-j)));
        }
    }

    completed++;
    if(completed % 1000 == 0) std::cout << "completed:" << completed << std::endl;

    return DP[a][b];
}

int main() {
    //dp(5,5);
    /*for(int a = 0; a <= 1000; a ++) dp(a,1000);
    std::cout << "done!" << std::endl;
    for(int i = 0; i <= 1000; i ++) {
        std::cout << "{";
        for(int j = 0; j <= 1000; j ++) std::cout << (j?", ":"") << DP[i][j];
        std::cout << "}," << std::endl;
    }
    return 0;*/
    int T;
    std::cin >> T;
    int C = 1;


    while(T--) {
        int t = 0;
        int D;
        std::cin >> D;
        VI DV(D,0);
        for(int i = 0; i < D; i ++) std::cin >> DV[i];

        std::sort(DV.begin(), DV.end());
        t = DV.back();

        // {3, 5, 7}
        // {3, 5, (7)}

        for(int target = 1; target <= DV.back(); target ++) {
            int req = 0;
            //std::cout << "Trying to get to target " << target << std::endl;
            for(int i = 0; i < D; i ++) {
                int *x = std::lower_bound(DP[DV[i]] + 0, DP[DV[i]] + 10, target, std::greater<int>());
                //std::cout << DV[i] << " needs " << x-DP[DV[i]] << " movements to get under" << std::endl;
                req += x-DP[DV[i]];
            }
            t = std::min(t, target+req);
        }

        /*while(remaining.size() > 0) {
            int hi = 0;
            for(int i = 0; i < remaining.size(); i ++) {
                if(remaining[i] == 0) { std::swap(remaining[i], remaining.back()); remaining.pop_back(); i --; }
                if(remaining[hi] < remaining[i]) hi = i;
            }
        }*/

        std::cout << "Case #" << (C++) << ": " << t << std::endl;
    }
    return 0;
}
