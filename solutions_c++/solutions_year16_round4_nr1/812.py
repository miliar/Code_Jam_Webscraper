#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T, n, p, r, s, a[5000];

string P[13], R[13], S[13];

string getmin(string a, string b) {
    return a+b<b+a?a+b:b+a;
}

void prepare() {
    P[0] = "P", S[0]="S", R[0]="R";
    for (int i = 1; i <= 12; ++ i) {
        P[i] = getmin(P[i-1], R[i-1]);
        R[i] = getmin(R[i-1], S[i-1]);
        S[i] = getmin(S[i-1], P[i-1]);
    }
}

bool check(string a) {
    int cr, cp, cs;
    cr = cp = cs = 0;
    for (int i = 0; i < (1 << n); ++ i)
        if (a[i] == 'R') cr ++ ;
        else if (a[i] == 'S') cs ++ ;
        else cp ++ ;
    return (cr == r) && (cp == p) && (cs == s);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>T;
    prepare();
    for (int ca = 1; ca <= T; ++ ca) {
        cin>>n>>r>>p>>s;
        string ans = "";
        if (check(P[n])) ans = P[n];
        if (check(R[n]) && (ans == "" || R[n] < ans)) ans = R[n];
        if (check(S[n]) && (ans == "" || S[n] < ans)) ans = S[n];
        if (ans == "") ans = "IMPOSSIBLE";
        cout<<"Case #" << ca<<": "<<ans<<endl;

    }
    return 0;
}
