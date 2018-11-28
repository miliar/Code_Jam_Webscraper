#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
using namespace std;

bool isPrime(long long p, long long &divisor) {
    for (int i = 2; i <= sqrt(p); i++) {
        long long div = p/i;
        if (i * div == p) {
            divisor = i;
            return false;
        }
    }
    return true;
}

long long convertBinToBase (long long coin, int base) {
    long long ans = 0;
    int p = 0;
    while (coin > 0) {
        ans += (coin&1)*pow(base, p);
        p++;
        coin = coin >> 1;
    }
    return ans;
}

vector<long long> computeDivisors(long long p) {
    vector<long long> divisors;
    for (int i = 2; i <= 10; i++) {
        long long b = convertBinToBase(p, i);
        long long divisor;
        isPrime(b, divisor);
        divisors.push_back(divisor);
    }
    return divisors;
}

bool isJamCoin(long long coin) {
    for (int i = 2; i <= 10; i++) {
        long long p = convertBinToBase(coin, i);
        long long divisor;
        if (isPrime(p, divisor))
            return false;
    }
    return true;
}

int main() {
    //    freopen("input.txt", "rt", stdin);
    //    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    
//    int N = 16;
//    int J = 50;

    int N;
    int J;
    cin >> N;
    cin >> J;
    
    int j = 0;
    long long i = 1 << (N-1);
    
    vector<long long> ans;
    
    while (j < J){
        if ((i%2 == 1) && isJamCoin(i)) {
            j++;
            ans.push_back(i);
        }
        i++;
    }
    
    vector<vector<long long> > ansDivisors;
    
    for (int k = 0; k < ans.size(); k++) {
        vector<long long> divisors = computeDivisors(ans[k]);
        ansDivisors.push_back(divisors);
    }
    
    cout << "Case #1:" << endl;
    for (int k = 0; k < ans.size(); k++) {
        bitset<16> x(ans[k]);
        cout << x << " ";
        for (int m = 0; m < ansDivisors[k].size(); m++)
            cout << ansDivisors[k][m] << " ";
        cout << endl;
    }
    
}

