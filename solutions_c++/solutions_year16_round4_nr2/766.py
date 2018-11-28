#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int T,N,K;
double P[222];

double GetProb(const vector<double> PP) {
    double ret = 0;
    for(int i = 0 ; i < (1<<K) ; i++ ) {
        if( __builtin_popcount(i)*2 != K ) {
            continue;
        }
        double s = 1.0;
        for(int j = 0 ; j < K ; j++ ) {
            if( (i>>j) & 1 ) {
                s *= PP[j];
            } else {
                s *= 1.0-PP[j];
            }
        }
        ret += s;
    }
    return ret;
}

int main() {
    scanf("%d",&T);
    int cases = 1;
    while( T-- ) {
        scanf("%d%d",&N,&K);
        for(int i = 0 ; i < N ;i++ ) scanf("%lf",&P[i]);
        double ans = 0;
        for(int i = 0 ; i < (1<<N); i++ ) {
            if( __builtin_popcount(i) != K) continue;
            vector<double> PP;
            for(int  j= 0 ; j < N; j++ ) {
                if( (i>>j)&1 ) {
                    PP.push_back(P[j]);
                }
            }
            ans = max(ans,GetProb(PP));
        }
        printf("Case #%d: %.8f\n",cases++,ans);
    }
    return 0;
}