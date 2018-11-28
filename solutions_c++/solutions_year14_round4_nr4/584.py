#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <assert.h>

using namespace std;

const long long mod = 1000000007;

long long doit(const vector<string>& v) {
    if (v.size() == 0) return 0;
    set<string> st;
    st.insert("");
    for (int i = 0; i < v.size() ; ++ i) {
        string q;
        string s = v[i];
//        reverse(s.begin(), s.end());
        for (int j = 0; j < s.size(); ++ j ) {
            q.push_back(s[j]);
            st.insert(q);
        }
    }
    return st.size();
}

pair<long long, long long> slow(int n, const vector<string>& v) {
    assert(n <= 4);
    vector<int> assign;
    long long a1 = 0, a2 = 0;
    for (int i = 0; i < v.size(); ++ i) assign.push_back(0);
    while (true) {
        vector<string> vv[4];
        for (int i = 0; i < v.size(); ++ i) {
            vv[assign[i]].push_back(v[i]);
        }
        long long b1 = 0;
        for (int i = 0; i < n; ++ i) {
            b1 += doit(vv[i]);
        }
        if (b1 > a1) {
            a1 = b1;
            a2 = 1;
        }
        else if (a1 == b1) {
            a2 ++;
        }

        // inc
        int i = 0; while (i < assign.size() && assign[i] == n - 1) {
            ++ i;
        }
        if (i == assign.size()) {
            break;
        }

        assign[i] ++;
        -- i;
        while (i >= 0) assign[i--] = 0;
    }
    return make_pair(a1, a2);
}

char buf[1005];
int main() {
    int t, tt;
    scanf("%d", &tt);
    for (t = 1; t <= tt; ++ t) {
        fprintf(stderr, "%d\n", t);
        printf("Case #%d: ", t);

        int n, m;
        scanf("%d %d", &n, &m);
        vector<string> v;
        for (int i = 0; i < n; ++ i) {
            scanf("%s", buf);
            v.push_back(buf);
        }
        pair<long long, long long> ans = slow(m, v);
        printf("%lld %lld", ans.first, ans.second);

        printf("\n");
    }

    return 0;
}
