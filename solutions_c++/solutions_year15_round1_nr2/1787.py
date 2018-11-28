//
//  main.cpp
//  haircut
//

#include <iostream>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

int gcd(int a, int b) {
    while (true) {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b) {
    int t = gcd(a, b);
    return t ? (a / t * b) : 0;
}

int bscnn(int arr[], int sz) {
    return accumulate(arr, arr+sz, 1, lcm);
}

int main() {
    freopen("B-small-attempt2.in.txt","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, pid=1;
    for (cin>>T;T--;) {
        cout << "Case #" << pid++ << ": ";
        int B, N;
        
        scanf("%d%d", &B,&N);
        int M[1001], m[1001];
        memset(m, 0, sizeof(int)*B);
        for (int i = 0; i < B; ++i) {
            cin>>M[i];
            m[i]=M[i];
        }
        
        int bsc = bscnn(m, B);
        int total = 0;
        for (int i = 0; i < B; ++i) {
            total += bsc / m[i];
        }
        
        N %= total;
        if (N == 0) N = total;
        
        if (B >= N) cout << N << endl;
        else {
            N-=B;
            while (N > 0) {
                bool canBreak = false;
                int mintime = 10000000;
                for (int i = 0; i < B; ++i)
                    if (mintime > m[i]) mintime = m[i];
                for (int i = 0; i < B; ++i) {
                    m[i] -= mintime;
                    if (0 == m[i]) {
                        N--, m[i] = M[i];
                        if (0 == N) {
                            cout << i+1 << endl;
                            canBreak = true;
                            break;
                        }
                    }
                    
                }
                if (canBreak)
                    break;
            }
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
