#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <math.h>
#include <numeric>
#include <iostream>
#include <utility>
#include <stack>
using namespace std;


const int MOD = 1000002013;

typedef long long i64;

typedef pair<i64, i64>  PII;

i64 N, M;

int Qi_idx=0, Qo_idx=0;
i64 Z=0, G=0;


i64 cost(i64 n) {
    // n + n - 1 + n - 2 + ..
    if(n&1) {
        return ( (n*N)%MOD - (((n-1)>>1)*n)%MOD ) % MOD;
    }
    return ( (n*N)%MOD - (((n-1))*(n>>1))%MOD ) % MOD;
}

int calc() {
    scanf("%lld%lld", &N, &M);
    Z = G = 0;
    vector<PII> Qi, Qo;
    for(int i=0; i<M; ++i) {
        i64  beg, end, num;
        scanf("%lld%lld%lld", &beg, &end, &num);
        Qi.push_back(make_pair(beg, num));
        Qo.push_back(make_pair(end, num));
        Z = (Z + cost(end-beg)*num % MOD) % MOD;
        // printf("{%lld:%lld:%lld} %lld\n", beg, end, num, cost(end-beg)*num);
    }
    // printf("Z = %lld\n", Z);
    sort(Qi.begin(), Qi.end());
    sort(Qo.begin(), Qo.end());
    vector<PII>  x;
    size_t  k = 0;
    for(size_t i=0; i<Qo.size(); ++i) {
        i64 at = Qo[i].first;
        i64 num = Qo[i].second;
        // printf("at=%lld num=%lld\n", at, num);
        for(; k<Qi.size() && Qi[k].first <= at; ++k) {
            x.push_back(Qi[k]);
        }
        while(num > 0) {
            PII  t = x.back(); x.pop_back();
            // printf("t = {%lld:%lld} %lld\n", t.first, t.second, cost(at-t.first)*min(t.second, num));
            if(t.second <= num) {
                num -= t.second;
                G = (G + cost(at-t.first) * t.second % MOD)%MOD;
            }
            else {
                t.second -= num;
                G = (G + cost(at-t.first) * num % MOD)%MOD;
                num = 0;
                x.push_back(t);
            }
            
        }
    }
    // printf("G = %lld\n", G);
    return ((Z - G)%MOD + MOD) % MOD;
}



int main(int argc, char* argv[]) {
    int  T;
    scanf("%d", &T);
    for(int it=1; it<=T; ++it) {
        printf("Case #%d: %d\n", it, calc());
    }
    return 0;
}

