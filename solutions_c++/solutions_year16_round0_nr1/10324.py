#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
 
using namespace std;
 
typedef vector<int> VI;
 
#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define ALL(c) (c).begin(),(c).end()

int readInt() { int n; if ( scanf("%d", &n) != 1 ) throw("invalid input"); return n; }

int solve(int N) {
    if (N == 0) return -1;
    VI v(10, 0); v[0] = 1000000;
    int tmp = N, i = 1;
    while(true) {
        while(tmp != 0) {
            v[tmp%10] = tmp%10;
            tmp /= 10;
        }
        if ( accumulate(ALL(v), int(0)) == 45 ) {
            return N*i;
        }
        i++;
        tmp = N * i;
    }
    return -1;
}

int main() {
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

    int T = readInt(), i = 0;

    FOR(i, 0, T) {
        int answer = solve(readInt());
        if (answer == -1)
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        else
            cout << "Case #" << i+1 << ": " << answer << endl;
    }
    
    return 0;
}