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
void solve(int ncase) {
    cout << "Case #"<< ncase << ": ";
    int n;
    cin >> n;
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    vector<int> exist(10);
    int nexist = 0;

    for(int i = 1; ; i++) {
        ostringstream oss;
        oss << n * i;
        for(auto c : oss.str()) {
            if (exist[c - '0'] == 0) {
                nexist++;
                exist[c - '0'] = 1;
            }
        }
        if (nexist == 10) {
            cout << n * i << endl;
            return;
        }
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
