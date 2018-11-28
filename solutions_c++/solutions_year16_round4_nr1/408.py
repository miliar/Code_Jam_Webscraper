#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long

/*
 * 1: RP PS SR
 *
 * 2: {RP, PS}, {RP, SR}, {PS, SR}
 *
 * 3: {{RP, PS}, {RP, SR}},  {{RP, PS}, {PS, SR}}, {{RP, SR}, {PS, SR}}
 *    {2PRS, 2RPS}, {2P, 2S}, {2S, 2R}
 *    3P3R2S, 3R3P2R, 3S3R2P
 *
 *
 *
 * 1: 1X1X0X
 *
 * 2: 2X1X1X
 *
 * 3: 3X3X2X
 *
 * 4: 6X5X5X
 *
 * 5: 11X11X10X
 *
 * 6: 22X21X21X
 *
 * 7: 43 43 42
 *
 * 8: 86 85 85
 *
 */

int N, R, P, S;

int mem[1<<20];
int v(int n) {
    if (n == 0) return 1;
    if (n == 1) return 1;
    int &ans = mem[n];
    if (ans != -1) return ans;

    ans = v(n-1);
    if (n%2 == 0) {
        return ans = ans *2;
    } else {
        return ans = ans*2 - 1;
    }
}


bool bad = false;
string solve(int P, int R, int S, int N) {
    if (N == 0) {
        if (P == 1 && R == 0 && S == 0) return "P";
        if (P == 0 && R == 1 && S == 0) return "R";
        if (P == 0 && R == 0 && S == 1) return "S";
        bad = true;
        return "IMPOSSIBLE";
    }
    
    int cur = v(N);
    int x = N%2;
    int o = cur - 1;
    int prev = v(N-1);
    int po = prev-1;

    //printf("N=%d, cur = %d, %d\n", N, cur, o);

    if (x) {
        // 2
        if (P == cur && R == cur && S == o) {
            return solve(prev, po, po, N-1) + solve(po, prev, po, N-1);
        }
        if (P == cur && R == o && S == cur) {
            return solve(prev, po, po, N-1) + solve(po, po, prev, N-1);
        }
        if (P == o && R == cur && S == cur) {
            return solve(po, prev, po, N-1) + solve(po, po, prev, N-1);
        }
        bad = true;
        return "";
        
    } else {
        if (P == cur && R == o && S == o) {
            return solve(prev, prev, po, N-1) + solve(prev, po, prev, N-1);
        }
        if (P == o && R == cur && S == o) {
            return solve(prev, prev, po, N-1) + solve(po, prev, prev, N-1);
        }
        if (P == o && R == o && S == cur) {
            return solve(prev, po, prev, N-1) + solve(po, prev, prev, N-1);
        }
        bad = true;
        return "";
    }
}


int main() {
    memset(mem,-1,sizeof(mem));
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        bad = false;
        cin>>N>>R>>P>>S;

        string out = solve(P, R, S, N);
        if (bad) out = "IMPOSSIBLE";

        printf("Case #%d: %s\n", t, out.c_str());
    }
}
