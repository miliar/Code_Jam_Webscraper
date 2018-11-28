#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;

const int MAX = 4;
int N;
std::string work[MAX];

unsigned int next(unsigned int v) {
    unsigned int t = v | (v - 1);
    return (t + 1) | (((~t & -~t) - 1) >> (__builtin_ctz(v) + 1));
}

bool pos(std::string chk[4], int cnt) {
    std::vector<int> ord;
    for(int i = 0; i < N; ++i)
        ord.push_back(i);

    bool acc[4];
    do {
        memset(acc, false, sizeof(acc));
        for(int w = 0; w < N; ++w) {
            int job = 0;
            for(int m = 0; m < N; ++m)
                if(chk[ord[w]][m] == '1') {
                    acc[m] = true;
                    ++job;
                }

            int sim = 0;
            for(int i = 0; i < N; ++i)
                if(chk[ord[w]] == chk[i]) ++sim;

            if(sim != job) return false;
        }

        for(int i = 0; i < N; ++i)
            if(!acc[i]) return false;
    } while(std::next_permutation(ord.begin(), ord.end()));

        // for(int i = 0; i < N; ++i)
        //     std::cout << chk[i] << std::endl;

    return true;
}

int brute() {
    int op = N * N;
    int best = op;
    std::string cur[4];
    for(int i = 0; i < (1<<op); ++i) {
        if(__builtin_popcount(i) >= best) continue;
        for(int j = 0; j < N; ++j)
            cur[j] = work[j];
        int cnt = 0;
        for(int j = 0; j < op; ++j) {
            if(i & (1<<j)) {
                int r = j / N;
                int c = j % N;
                cur[r][c] = '1';
                ++cnt;
            }
        }

        if(pos(cur, cnt)) best = std::min(best, cnt);
    }
    return best;
}

int main() {
    int CS;
    std::cin >> CS;
    // std::cout << std::fixed << std::setprecision(8);
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N;
        for(int n = 0; n < N; ++n) 
            std::cin >> work[n];

        int ans = brute();
        std::cout << "Case #" << cs << ": " << brute() << std::endl;
    }
}
