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
    string s;
    cin >> s;
    int len = s.length();
    int res = 0;
    FOR(i, 1, len - 1) {
        if (s[i] != s[i - 1]) ++res;
    }
    if (s[len - 1] == '-') ++res;
    cout << res << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
