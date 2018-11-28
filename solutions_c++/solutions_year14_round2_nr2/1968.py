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

int A, B, K;

int main(){
    int T;
    std::cin >> T;

    FOR(_, 1, T+1){
        std::cin >> A >> B >> K;

        int res = 0;
        REP(a, A){
            REP(b, B){
                if((a & b) < K){res += 1;}
            }
        }

        printf("Case #%d: %d\n", _, res);
    }
}
