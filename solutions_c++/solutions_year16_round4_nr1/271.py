#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
// 0 1 2 P R S

string calc(int dep, int x) {
    if (dep == 0) {
        if (x == 0) return "P";
        if (x == 1) return "R";
        if (x == 2) return "S";
    }
    if (x == 0) {
        string a =  calc(dep-1,0);
        string b =  calc(dep-1,1);
        if (a < b) return a + b;
        else return b + a;
    }
    if (x == 1) {
        string a =  calc(dep-1,1);
        string b =  calc(dep-1,2);
        if (a < b) return a + b;
        else return b + a;
    }
    string a =  calc(dep-1,0);
    string b =  calc(dep-1,2);
    if (a < b) return a + b;
       else return b + a;
}

bool ok(string A, int r, int p, int s){
    int rr=0,pp=0,ss=0;
    for (int i = 0; i < A.size(); i++) {
        if (A[i]=='R') rr++;
        if (A[i]=='P') pp++;
        if (A[i]=='S') ss++;
    }
    return r==rr&&p==pp&&s==ss;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-l.out", "w", stdout);
    int testcase, N, R, P, S;
    cin >> testcase;
    for (int o = 1; o <= testcase; o++) {
        printf("Case #%d: ", o);
        cin >> N >> R >> P >> S;
        string a = calc(N, 0);
        string b = calc(N, 1);
        string c = calc(N, 2);
        string ans = "";
        if (ok(a, R, P, S)) {
            if (ans==""||a<ans) ans = a;
        }
        if (ok(b, R, P, S)) {
            if (ans==""||b<ans) ans = b;
        }
        if (ok(c, R, P, S)) {
            if (ans==""||c<ans) ans = c;
        }
        if (ans=="")
            cout <<"IMPOSSIBLE"<< endl;
        else cout << ans << endl;
    }
}
