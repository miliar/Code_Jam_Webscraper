#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>

using namespace std;

long long pow0(int K, int C) {
    long long res = 1;
    for (int i = 1; i <= C; ++i)
        res *= K;
    return res;
}

int main(){
	ios::sync_with_stdio(false);
	int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        int K, C, S;
        cin>>K>>C>>S;
        printf("Case #%d: ", t);
        if (K == 1) {
            printf("1\n");
            continue;
        }
        
        if (C == 1) {
            for (int i = 1; i <= K; ++i)
                printf((i == K) ? "%d\n" : "%d ", i);
            continue;
        }
        
        long long C1 = pow0(K, C - 1);
        for (int i = 1; i <= K; ++i) {
            long long C0 = (C1 - 1) / (K - 1) * (i - K);
            printf((i == K) ? "%lld\n" : "%lld ", C1 * i + C0);
        }
    }
	return 0;
}