#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

int ans;

string hashval(const vi& v) {
    vi t = v;
    sort(t.begin(), t.end());

    ostringstream ss;
    For(i, t.size()) {
        assert(0 <= t[i] && t[i] <= 9);
        if (t[i] == 0) continue;
        ss << t[i];
    }
    return ss.str();
}

void bruteforce(int time, const vi& v, map<string, int>& memo) {
    bool empty = true;
    For(i, v.size()) {
        if (v[i] > 0) {
            empty = false;
            break;
        }
    }

    if (empty) {
        ans = min(ans, time);
        return;
    }

    string h = hashval(v);
    int x = memo[h];
    if (x > 0 && time >= x) {
//        printf("cached hash:%s x:%d time:%d\n", h.c_str(), x, time);
        return;
    }
    memo[h] = time;

    vi t = v;
    For(i, t.size()) t[i] = max(0, t[i]-1);
    bruteforce(time+1, t, memo);

    // パンを移す
    For(i, t.size()) t[i] = v[i];
    For(i, t.size()) {
        if (t[i] >= 4) { // パンは 4 つ以上ないと移す意味ない
            int ti = t[i];
            for (int j = 2; j < ti; j++) { // j 個うつす
                if (j > (ti-j)) break;
                t[i] = j;
                t.push_back(ti - j);
                bruteforce(time+1, t, memo);
                t[i] = ti;
                t.pop_back();
            }
        }
    }
}

int calc(const vi& v) {
    ans = INT_MAX;
    map<string, int> memo;
    bruteforce(0, v, memo);
    return ans;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n;
        scanf("%d", &n);
        vi v(n);
        For(i, n) scanf("%d", &v[i]);

        printf("Case #%d: %d\n", cc+1, calc(v));
    }
}

