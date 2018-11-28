#include <cstdio>
#include <climits>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#define ULL unsigned long long

using namespace std;

ULL qpow(int a, int b){
    ULL num = 1, mul = a;
    for(; b; mul *= mul, b >>= 1) if(b & 1) num *= mul;
    return num;
}


int main(void){
    int T, k, c, s, kase = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d %d %d", &k, &c, &s);
        cout << "Case #" << ++kase << ": ";
        ULL num;
        for(int i = 1; i <= k; i++){
            num = 1 + (i - 1) * qpow(k, c - 1);
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}

