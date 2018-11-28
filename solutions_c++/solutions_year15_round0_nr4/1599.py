#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<string>

using namespace std;

string solve() {
    int x, r, c;
    cin >> x >> r >> c;

    if(r*c % x != 0) return "RICHARD";

    if(x <= 2) return "GABRIEL";

    if(x >= 7) return "RICHARD";

    if(r < c) swap(r,c);

    if((x+1)/2 > c) return "RICHARD";
    if(x > r) return "RICHARD";

    if(x == 3) {
        if(c == 1) return "RICHARD";
        else return "GABRIEL";
    }

    if(x == 4) {
        if(c<=2) return "RICHARD";
        else return "GABRIEL";
    }

    return "RICHARD";
}

int main() {
    freopen("Din.txt", "r", stdin);
    freopen("Dout.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int i=1; i<=T; i++) {
        printf("Case #%d: %s\n", i, solve().c_str());
    }

    return 0;
}
