#include <iostream>
#include <map>
#include <set>
using namespace std;
long long calccould(int N, long long P) {
    long long teams = 1LL<<N;
    for (int win=0; win<=N; win++) {
        // if we win this many games, do we win a prize?
        if (P>=teams) {
            return (1LL<<N) - (1LL<<win);
        } else {
            teams/=2;
        }
    }
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        int N; scanf("%d",&N);
        long long P; scanf("%I64d",&P);
        
        long long A,B;
        if (P==(1LL<<N)) {
            A = B = P-1;
        } else {
            A = (1LL<<N)-2-calccould(N,(1LL<<N)-P);
            B = calccould(N,P);
        }
        printf("Case #%d: %I64d %I64d\n",t,A,B);   
    }
}
