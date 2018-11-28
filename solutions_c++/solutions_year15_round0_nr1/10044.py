#include <iostream>
#include <fstream>
#include <string>
 
using namespace std;
 
#define FOR(i, a, b) for(i = (a); i < (b); ++i)

int readInt() { int n; if ( scanf("%d", &n) != 1 ) throw("invalid input"); return n; }
string readString() { static char sz[100000]; if ( scanf("%s",sz) != 1 ) throw("invalid input"); return sz; }

int solve() {
    string str; char c;
    int i = 0, N = readInt() + 1, s = 0, ans = 0;

    str = readString();
    FOR(i, 0, N) {
        c = str[i];
        if (s>=i) {
            s+= atoi(&c);
        }
        else if (s < i && atoi(&c) > 0) {
            ans += i-s;
            s += (i-s) + atoi(&c);
        }
    }
    return ans;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);    
    int T = readInt(), i = 0;
    FOR(i, 0, T) {
        cout << "Case #" << i+1 << ": " << solve() << endl;
    }    
    return 0;
}