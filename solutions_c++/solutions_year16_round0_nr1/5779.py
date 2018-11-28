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

string solve() {
    long long n;
    cin >> n;
    
    unordered_set<int> digits;
    
    for (long long i = 1; i < 10000000; ++i) {
        long long nn = n * i;
        while (nn) {
            digits.insert(nn % 10l);
            nn/=10l;
        }
        if (digits.size() == 10) {
            return to_string(n * i);
        }
    }
    return "INSOMNIA";
    
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    
    
    return 0;
}