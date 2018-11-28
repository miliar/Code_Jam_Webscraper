#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <queue>

using namespace std;

struct mlp {
    char x;
    bool mns;
    mlp() {
        x = '1';
        mns = false;
    }
    mlp(char c, bool sgn) {
        x = c;
        mns = sgn;
    }
    mlp operator *(const mlp &sc) {
        mlp res;
        if (x == '1') {
            res.x = sc.x;
        }
        if (x == 'i') {
            if (sc.x == '1') {
                res.x = 'i';
            }
            if (sc.x == 'i') {
                res.x = '1';
                res.mns ^= true;
            }
            if (sc.x == 'j') {
                res.x = 'k';
            }
            if (sc.x == 'k') {
                res.x = 'j';
                res.mns ^= true;
            }
        }
        if (x == 'j') {
            if (sc.x == '1') {
                res.x = 'j';
            }
            if (sc.x == 'i') {
                res.x = 'k';
                res.mns ^= true;
            }
            if (sc.x == 'j') {
                res.x = '1';
                res.mns ^= true;
            }
            if (sc.x == 'k') {
                res.x = 'i';
            }
        }
        if (x == 'k') {
            if (sc.x == '1') {
                res.x = 'k';
            }
            if (sc.x == 'i') {
                res.x = 'j';
            }
            if (sc.x == 'j') {
                res.x = 'i';
                res.mns ^= true;
            }
            if (sc.x == 'k') {
                res.x = '1';
                res.mns ^= true;
            }
        }
        res.mns ^= mns;
        res.mns ^= sc.mns;
        return res;
    }
};
string s;
int rep, len;
string solve() {
    cin>>len>>rep;
    string t;
    cin>>t;
    s = "";
    for (int i = 1; i <= rep; i++) {
        s += t;
    }
    int I = -1;
    mlp i1('1', false);
    for (int i = 0; i < s.length(); i++) {
        i1 = i1*mlp(s[i], false);
        if (i1.x == 'i' && i1.mns == false) {
            I = i;
            break;
        }
    }
    if (I == -1) {
        return "NO";
    }
    int J = -1;
    mlp j1('1', false);
    for (int i = I + 1; i < s.length(); i++) {
        j1 = j1*mlp(s[i], false);
        if (j1.x == 'j' && j1.mns == false) {
            J = i;
            break;
        }
    }
    if (J == -1) {
        return "NO";
    }
    mlp k1('1', false);
    for (int i = J + 1; i < s.length(); i++) {
        k1 = k1*mlp(s[i], false);
    }
    if (k1.x == 'k' && k1.mns == false) {
        return "YES";
    }
    else {
        return "NO";
    }
}

int main() {
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        cout<<"Case #"<<i<<": "<<solve()<<"\n";
    }
    return 0;
}
