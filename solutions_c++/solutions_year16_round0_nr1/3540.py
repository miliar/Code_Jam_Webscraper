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

string i2s(LL n) {
    stringstream ss;
    ss << n;
    string res;
    ss >> res;
    return res;
}

void run() {
    LL n;
    cin >> n;

    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    int v[10] = { 0 };
    LL cur = 0, num = 0;
    while (true) {
        cur += n;
        string s = i2s(cur);
        for (int i = 0; i < s.length(); ++i) {
            int d = s[i] - '0';
            if (v[d] == 0) {
                ++num;
                v[d] = 1;
            }
        }
        if (num == 10) break;
    }

    cout << cur << endl;
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
