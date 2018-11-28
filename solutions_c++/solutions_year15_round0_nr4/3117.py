#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <stack>
#include <set>
#include <map>

using namespace std;

#ifdef DEBUG
    #define DBG(x) cerr<<#x<<"="<<(x)<<'\n'
#else
    #define DBG(x) static_cast<void>(0)
#endif

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i) ++)

bool solve(int x, int r, int c) {
    if (r > c)
        swap(r, c);
    return ((r * c) % x != 0) || (r < x && c < x) || (x > 6) || (r <= x-2);
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    in >> T;
    REP1(I,T) {
        cerr<<I<<"\n";
        int x,r,c;
        in >> x >> r >> c;
        out<<"Case #"<<I<<": ";
        if (solve(x, r, c))
            out<<"RICHARD\n";
        else
            out<<"GABRIEL\n";
    }

    in.close();
    out.close();
    return 0;
}
