/*
 * D.Fractiles.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: piotr
 */

#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void find_solution(int K, int C, int S);

int main() {
    clog.tie(&cout);

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << case_num << ":";
        find_solution(K, C, S);
        cout << endl;
    }
    return 0;
}

/* 0-based
 * A tile of coordinates (a1,...,ac) has position
 * sum_{j=1}^C aj*K^(C-j).
 * Take (0,1,...,C-1), (C+1,C+2,...,2C-1),...,((S-1)C,...,SC-1)
 */

void test(int K, int C, int S, const vector<unsigned long long> & res) {
    if(C*S < K)
        clog << "ERROR 1, ";
    vector<char> check(K, 0);
    for(auto r : res) {
        for(auto c = 0; c < C; ++c) {
            auto a = r%K;
            check[a] = 1;
            r -= a;
            r /= K;
        }
    }
    for(auto c: check)
        if(!c)
            clog << "ERROR 2" << endl;
    for(auto i = 1u; i < res.size(); ++i)
        if(res[i] < res[i-1]) {
            clog << "ERROR: Not monotonic" << endl;
            break;
        }
    auto M = 1ull;
    for(auto i = 0; i<C; ++i)
        M *= K;
    if(res.back() >= M)
        clog << "ERROR: range" << endl;
}

void find_solution(int K, int C, int S){
    if(C*S < K) {
        cout << "IMPOSSIBLE";
        return;
    }
    vector<unsigned long long> results;
    for(auto s = 1, aj = 0; s <= S && aj < K; ++s) {
        auto x = 0ull;
        for(auto j = 1; j <= C; ++j, ++aj) {
            // Caveat: double arithmetic in pow
//            x +=   min(aj,K-1) * pow(1ull*K, C-j);
            x *= K;
            x += min(aj, K-1);
        }
        results.push_back(x);
    }
    for(auto r : results)
        cout << " " << r+1;
}




