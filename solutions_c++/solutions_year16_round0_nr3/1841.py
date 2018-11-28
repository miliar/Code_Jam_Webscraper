#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
#include <list>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> PII;
typedef pair<int, double> PID;
typedef pair<string, int> PSI;
typedef pair<string, string> PSS;
typedef pair<PII, int> PIP;
void precalc(){};
string bin(ll x) {
    string ret;
    while(x) {
        ret.push_back(x % 2 + '0');
        x /= 2;
    }
    std::reverse(ret.begin(), ret.end());
    return ret;
}

bool check(int z) {
    string binstr = bin(z);
    for(int i = 2; i <= 10; i ++) {
        ll num = 0;
        ll w = 1;
        for(int j = 0; j < binstr.size(); j ++) {
            if (binstr[binstr.size() - 1 - j] == '1') {
                num += w;
                num %= (i+1);
            }
            w *= i;
            w %= (i + 1);
        }
        if (num != 0) return false;
    }
    return true;
}

void solve(int ncase) {
    cout << "Case #" << ncase << ":\n";
    int n, j;
    cin >> n >> j;
    ll z = (1LL<<n)/3*3;
    for(int i = 0; i < j; i ++) {
        cout << bin(z) << " 3 4 5 6 7 8 9 10 11" << endl;
        z -= 6;
        while(!check(z))z -= 6;
    }
}
int main() {
    //ios::sync_with_stdio(false);
    //cout << std::fixed << setprecision(16);
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("A-small-practice.in", "r", stdin);
    //freopen("A-large-practice.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif
    int T = 1;
    //precalc();
    //cin >> T;
    scanf("%d", &T);
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
