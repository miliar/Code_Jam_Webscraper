#include <iostream>
#include <bitset>
#include <sstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

long long mod = 1000000007;

long long is_prime(long long num) {
    for (long long i = 2; i * i <=num; ++i) {
        if (num % i == 0) return i;
    }
    return -1;
}

long long convert_to(long long num, long long base) {
    if (base == 2) return num;
    
    long long res = 0;
    long long pow = 1;
    while (num) {
        if (num & 1) {
            res += pow;
        }
        pow *= base;
        num >>= 1;
    }
    
    return res;
}

void solve() {
    int n,j;
    cin >> n >> j;
    
    long long num = (1LL << (n - 1));
    
    while (num < (1LL << n) && j > 0) {
        if ((num & 1) == 0) {
            num++;
            continue;
        }
        
        bool is_nice = true;
        vector<long long> base_nums;
        vector<long long> factor_nums;
        for (int base = 2; base <= 10; ++base) {
            base_nums.push_back(convert_to(num, base));
            
            long long factor = is_prime(base_nums.back());
            factor_nums.push_back(factor);
            
            if (factor == -1) {
                is_nice = false;
                break;
            }
        }
        
        if (is_nice) {
            cout << bitset<16>(num);
            for (long long nn: factor_nums) {
                cout << " " << nn;
            }
            cout << endl;
            j--;
        }
        
        num++;
    }
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        cout << "Case #" << i << ":" << endl;
        solve();
    }
    
    
    return 0;
}