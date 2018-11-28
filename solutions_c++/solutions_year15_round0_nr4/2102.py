#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <set>
#include <map>

using namespace std;

const string no = "RICHARD";
const string yes = "GABRIEL";
string solve() {;
    int x, r, c;
    cin>>x>>r>>c;
    if (r > c) swap(r, c);
    if (x > c) {
        return no;
    }

    if (r*c%x != 0) {
        return no;
    }
    if (x == 3) {
        if (r == 1) {
            return no;
        }
    }
    if (x == 4) {
        if (r <= 2) {
            return no;
        }

    }
    return yes;
}

int main() {
    freopen("D-small2.in", "r", stdin);
    freopen("D-small2.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        cout<<"Case #"<<i<<": "<<solve()<<"\n";
    }
    return 0;
}
