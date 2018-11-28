#include<stdio.h>
#include<string>
using namespace std;
#define N 12
int t, n, r, p, s;
int R[N+1], P[N+1], S[N+1];
string solve(int n, int p, int s, int r) {
    if(n == 0) {
        if(p == 1) return string("P");
        if(s == 1) return string("S");
        if(r == 1) return string("R");
    }
    string r1, r2;
    if(p == 1) {
        r1 = solve(n-1, 1, 0, 0);
        r2 = solve(n-1, 0, 0, 1);
    }
    else if(s == 1) {
        r1 = solve(n-1, 1, 0, 0);
        r2 = solve(n-1, 0, 1, 0);
    }
    else if(r == 1) {
        r1 = solve(n-1, 0, 1, 0);
        r2 = solve(n-1, 0, 0, 1);
    }
    if(r1 < r2) return r1+r2;
    return r2+r1;
}
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &t);
    for(int i = 0; i < t; ++i) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        R[0] = r; P[0] = p; S[0] = s;
        int flag = 1;
        for(int j = 1; j <= n; ++j) {
            P[j] = R[j-1] + P[j-1] - (R[j-1]+P[j-1]+S[j-1])/2;
            S[j] = P[j-1] + S[j-1] - (R[j-1]+P[j-1]+S[j-1])/2;
            R[j] = R[j-1] + S[j-1] - (R[j-1]+P[j-1]+S[j-1])/2;
            if(P[j] < 0 || S[j] < 0 || R[j] < 0) flag = 0;
        }
        if(flag == 0) printf("Case #%d: IMPOSSIBLE\n", i+1);
        else printf("Case #%d: %s\n", i+1, solve(n, P[n], S[n], R[n]).c_str());
    }
    return 0;
}
