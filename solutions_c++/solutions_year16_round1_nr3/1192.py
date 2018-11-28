#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

bool isok(int N, vector<int>& bef, vector<int>& a) {
    int sz = a.size();

    if (sz == 1) return false;
    
    vector<int> t(sz);
    REP(i, sz) t[i] = a[i];
    sort(t.begin(), t.end());
    do {
        bool valid = true;
        REP(i, sz) {
            if (bef[t[i]] != t[(i + 1) % sz] && bef[t[i]] != t[(i - 1 + sz) % sz]) {
                valid = false;
                break;
            }
        }
        if (valid) return true;
    } while (next_permutation(t.begin(), t.end()));
    return false;
    
    /*vector<int> v(N, 0);
    REP(i, sz) v[a[i]] = 1;
    deque<int> que;
    que.push_back(a[0]);
    v[a[0]] = 0;
    int f = bef[a[0]];
    if (v[f] == 0) return false;
    que.push_back(f);
    v[f] = 0;
    while (que.size() < sz) {
        int len = que.size();
        int last = que[len - 1];
        int lastF = bef[last];
        if (lastF == que[len - 2]) {
            bool found = false;
            REP(i, sz) {
                if (v[a[i]] == 0) continue;
                if (bef[a[i]] == que[0]) {
                    found = true;
                    que.push_front(a[i]);
                    v[a[i]] = 0;
                    break;
                }
                if (bef[a[i]] == que[len - 1]) {
                    found = true;
                    que.push_back(a[i]);
                    v[a[i]] = 0;
                    break;
                }
            }
            if (!found) return false;
        }
        else {
            if (v[lastF] == 0) return false;
            que.push_back(lastF);
            v[lastF] = 0;
        }
    }

    if (bef[que[sz - 1]] != que[0] && bef[que[sz - 1]] != que[sz - 2]) return false;*/

    /*cout << endl << "*****" << endl;
    REP(i,sz) cout << que[i] << " ";
    cout << endl;
    REP(i,sz) cout << bef[que[i]] << " ";
    cout << endl;*/

    //return true;
}

void run() {
    int N;
    cin >> N;
    vector<int> bef(N);
    REP(i, N) {
        cin >> bef[i];
        --bef[i];
    }

    int res = 0;
    RFOR(st, (1 << N) - 1, 1) {
        vector<int> a;
        REP(i, N) {
            if (st & (1 << i)) a.push_back(i);
        }
        if (a.size() <= res) continue;
        if (isok(N, bef, a)) res = a.size();
    }

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
