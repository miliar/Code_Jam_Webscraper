#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;

int T, A, B, K;

int getLastBit(int N) {
    int n = 0;
    while (N != 0) {
        n++;
        N = N >> 1;
    }
    
    return n;
} 

long long solve() {
    long long r = 0;
    if (B < A) swap(A, B);
    
    int limA = min(A, K), limB = min(B, K);
    
    r += limA * B;
    r += limB * (A - limA);
    
    int bit1 = getLastBit(limA), bit2 = getLastBit(B-1);
    cout << bit1 << " " << bit2 << endl;
    
    r += ((1 << (bit2 - bit1)) - 1) * (A - limA);
    
    return r;
}

long long solveMal() {
    long long r = 0; 
    
    for (int i = 0; i < A; i++) {
        for (int j = 0; j< B; j++) {
            if ((i & j) < K) r++;
        }
    }
    
    return r;
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> A >> B >> K;
        printf("Case #%d: %lld\n", i+1, solveMal());
    }
    return 0;
}
