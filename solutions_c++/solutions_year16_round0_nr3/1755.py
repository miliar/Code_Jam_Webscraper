#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <utility>
#include <cassert>

typedef long long ll;
typedef std::pair<int, int> pii;

int N, J;
ll pows[11][20];
std::vector<ll> primes;

void small();

int force[9] = { 3, 2, 3, 2, 7, 2, 3, 2, 3 };
void print_set() {
    for(int i = 0; i < 9; ++i)
        std::cout << " " << force[i];
    std::cout << std::endl;
}

void solve() {
    const int TOP = N - 2;
    int tot = 0;
    for(int i = 1; i < (1<<TOP); ++i) {
        std::string test;
        int cnt = 0, cntOth = 0;
        for(int j = 0; j < TOP; ++j) {
            if(i & (1<<j)) {
                test += '1';
                ++cnt;
                if(j & 1) {
                    cntOth++;
                } else {
                    cntOth--;
                }
            } 
            else test += '0';
        }
        if((cnt + 2) % 6) continue;
        if(cntOth) continue;
        test = '1' + test + '1';
        std::reverse(test.begin(), test.end());

        std::cout << test;
        print_set();
        ++tot;
        if(tot >= J) break;
    }
}


int main() {
    int CS;
    std::cin >> CS;
    assert(CS == 1);
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> J;

        std::cout << "Case #" << cs << ":" << std::endl;
        // small();
        solve();
    }

    return 0;
}








ll prime(ll x) {
    int p = 0;
    while(p < primes.size() && primes[p] * primes[p] <= x) {
        if(x % primes[p] == 0) 
            return primes[p];
        ++p;
    }
    return -1;
}

void getPrimes() {
    std::ifstream p ("primes.txt");
    int buf;
    while(p >> buf)
        primes.push_back(buf);
}
void small() {
    getPrimes();
    
    for(int i = 2; i <= 10; ++i) {
        pows[i][0] = 1;
        for(int j = 1; j < 20; ++j)
            pows[i][j] = pows[i][j - 1] * i;
    }

    int count = 0;
    for(int i = 1; i < (1<<N); ++i) {
        if(!(i & 1)) continue;
        if(!(i & (1<<(N - 1)))) continue;
        // if(__builtin_popcountll(i) != 4) continue;
        ll cur;
        std::vector<ll> here;
        for(int bs = 2; bs <= 10; ++bs) {
            cur = 0;
            for(int j = 0; j < N; ++j)
                if(i & (1<<j))
                    cur += pows[bs][j];

            // std::cout << cur << std::endl;
            ll divi = prime(cur);
            if(divi == -1) goto nope;
            if(bs == 2 && divi != 3) goto nope;
            if(bs == 3 && divi != 2) goto nope;
            if(bs == 4 && divi != 3) goto nope;
            if(bs == 5 && divi != 2) goto nope;
            if(bs == 6 && divi != 7) goto nope;
            if(bs == 7 && divi != 2) goto nope;
            if(bs == 8 && divi != 3) goto nope;
            if(bs == 9 && divi != 2) goto nope;
            if(bs == 10 && divi != 3) goto nope;
            here.push_back(divi);
        }

        std::cout << cur;
        for(int i = 0; i < here.size(); ++i)
            std::cout << " " << here[i];
        std::cout << std::endl;
        ++count;
        // if(count >= J) break;
nope:;
    }
    std::cout << count << std::endl;
}
