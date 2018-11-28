#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <cstring>
#include <fstream>

using namespace std;

int n, R, P, S;
string res;
string str;

inline bool beats(char a, char b) {
    int A, B;
    A = (a=='R') + (a=='S')*2;
    B = (b=='R') + (b=='S')*2;
    return (A+1)%3 == B;
}

bool check() {
    string cur = str;
    string next;
    while(cur.size() > 1) {
        next = "";
        for(int i=0; i<cur.size(); i += 2) {
            if (cur[i] == cur[i+1]) return false;
            if (beats(cur[i], cur[i+1])) next += cur[i];
            else next += cur[i+1];
        }
        cur = next;
    }
    return true;
}

void rec(int p, int r, int s) {
    if (p == 0 && r == 0 && s == 0) {
        if (check() && (res == "" || str < res)) {
            res = str;
        }
        return;
    }
    if (p > 0) {
        str += 'P';
        rec(p-1, r, s);
        str = str.substr(0, str.size()-1);
    }
    if (r > 0) {
        str += 'R';
        rec(p, r-1, s);
        str = str.substr(0, str.size()-1);
    }
    if (s > 0) {
        str += 'S';
        rec(p, r, s-1);
        str = str.substr(0, str.size()-1);
    }
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, NT, i, j;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>n>>R>>P>>S;
        res = "";
        str = "";
        rec(P, R, S);
        if (res == "") res = "IMPOSSIBLE";
        cout<<"Case #"<<T<<": "<<res<<endl;
    }

    return 0;
}
