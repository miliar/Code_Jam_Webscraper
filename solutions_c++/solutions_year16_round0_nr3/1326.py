/*
 * C.CoinJam.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: piotr
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void find_solution(int N, int J);
int N, J;

int main() {

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        cin >> N >> J;
        cout << "Case #" << case_num << ":\n";
        find_solution(N,J);
    }
    return 0;
}

/*
 * Two consecutive 1's yield a k-based number divisible by k+1.
 * We place two 1's at the beginning and two at the end of the number,
 * add sequentially next pairs of 1's between and fill by zeros.
 */

void find_solution(int N, int J){
    assert(N > 3);
    vector<int> divisors (11);
    for(auto i = 2; i < 11; ++i)
        divisors[i] = i+1;
//    while(J > 0) {
        // 4 + 2*i = number of digits 1,
        // N-4-2*i = number of digits 0:
        for(auto i = 0; 2*i <= N-4 && J>0; ++i) {
            vector<int> digits(N-4-2*i, 0);
            digits.insert(digits.end(), i, 1);
            do {
                string ret (N, '1');
                for(auto j = 0u, k = 2u; j < digits.size(); ++j)
                    if(digits[j] == 0)
                        ret[k++] = '0';
                    else
                        k+=2;
                cout << ret;
                for(auto j = 2; j< 11; ++j)
                    cout << " " << divisors[j];
                cout << endl;
                --J;
            } while(next_permutation(digits.begin(), digits.end()) && J > 0);
//        }
    }
}

