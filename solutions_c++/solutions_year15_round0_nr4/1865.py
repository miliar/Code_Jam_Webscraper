#include <bits/stdc++.h>

using namespace std;

#define     mp              make_pair
#define     fs              first
#define     sc              second
#define     pob             pop_back
#define     pub             push_back
#define     eps             1E-7
#define     sz(a)           a.size()
#define     count_one       __builtin_popcount;
#define     count_onell     __builtin_popcountll;
#define     fastIO          ios_base::sync_with_stdio(false)
#define     PI              (acos(-1.0))
#define     linf            (1LL<<62)//>4e18
#define     inf             (0x7f7f7f7f)//>2e9

#ifndef ONLINE_JUDGE
ifstream fin("D:/C++/in");
ofstream fout("D:/C++/out");
#endif

const int MAXN = 100;

int T, x, r, c;

string solve() {
    bool canSolve = false;

    if(x == 1)
        canSolve = true;

    if(x == 2)
        if(r * c % 2 == 0)
            canSolve = true;
    if(x == 3)
        if(r * c % 3 == 0 && r > 1 && c > 1)
            canSolve = true;

    if(x == 4) {
        if((c == 4 && (r == 3 || r== 4)) || ((c == 3 || c == 4) && r == 4))
            canSolve = true;

    }

    if(canSolve)
        return "GABRIEL";
    return "RICHARD";
}

void read() {
	fin >> T;
	for(int t = 1; t <= T; ++t) {
        fin >> x >> r >> c;
        fout << "Case #" << t << ": " << solve() << "\n";
	}
}

int main() {
	read();

    return 0;
}
