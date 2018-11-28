#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,j) FOR(i,0,j)
#define mp std::make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int,int> P;
typedef std::pair<int,P> State;

const int INF = 1001001001;

// S N E W(南北東西)
const int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1}, dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

double A[1000001], B[1000001];

int main(){
    int T;
    scanf("%d", &T);
 
    FOR(_, 1, T+1){
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);

        A[0] = 2.0; B[0] = 0.0;
        FOR(i, 1, 1000001){
            A[i] = A[i-1] + F;
            B[i] = B[i-1] + C / A[i-1];
        }

        double mn = 1e10;
        REP(i, 1000001){
            mn = std::min(mn, B[i] + X / A[i]);
        }

        printf("Case #%d: %.7f\n", _, mn);
    }
}
