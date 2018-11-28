#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

void run() {
    int K, C, S;
    cin >> K >> C >> S;
    FOR(i,1,K) {
        LL idx = i;
        FOR(j,2,C) idx = (idx - 1) * K + i;
        cout << " " << idx;
    }
    cout << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ":";
        run();
    }
    return 0;
}
