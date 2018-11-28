#include <stdint.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

typedef std::vector<int> VI;
typedef std::vector<VI> VVI;
typedef std::pair<int, int> II;
typedef std::vector<II> VII;
typedef std::vector<VII> VVII;
typedef std::set<int> SI;

int move(VI &A, int a, int b) {
    int dir = 1;
    if(a > b) dir = -1;
    int cost = 0;
    while(a != b) {
        std::swap(A[a], A[a+dir]);
        a += dir;
        cost ++;
    }
    return cost;
}

int main() {
    int T;
    std::cin >> T;
    int C = 1;
    while(T--) {
        int N;
        std::cin >> N;
        VI A(N,0);
        for(int i = 0; i < N; i ++) {
            std::cin >> A[i];
        }

        int maxi = 0;
        for(int i = 1; i < N; i ++) {
            if(A[i] > A[maxi]) maxi = i;
        }

        VI As = A;
        std::sort(As.begin(), As.end());

        std::map<int, int> which;
        for(int i = 0; i < N; i ++) which[As[i]] = i;

        int best = 1<<25;
        for(int decisions = 0; decisions < (1<<N); decisions ++) {
            VI left;
            VI right;
            for(int i = 0; i < N; i ++) {
                if(decisions & (1<<i)) right.push_back(A[i]);
                else left.push_back(A[i]);
            }
            std::sort(left.begin(), left.end());
            std::sort(right.begin(), right.end(), std::greater<int>());

            VI ideal = left;
            for(auto r : right) ideal.push_back(r);
            //std::cout << "Target:";
            //for(int i = 0; i < ideal.size(); i ++) std::cout<< " " << ideal[i];
            //std::cout << std::endl;

            VI a = A;
            int cost = 0;
            for(int i = 0; i < N; i ++) {
                int where = -1;
                for(int j = 0; j < N; j ++) if(a[j] == ideal[i]) { where = j; }

                while(where > i) {
                    std::swap(a[where], a[where-1]);
                    where --;
                    cost ++;
                }
            }
            //std::cout << "\tcost: " << cost << std::endl;

            best = std::min(best, cost);
        }

        std::cout << "Case #" << C++ << ": " << best << std::endl;
    }
    return 0;
}
