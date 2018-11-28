#include <iostream>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <climits>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int T, n, m, C, cs = 0;
multiset<int> st;

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    while (T--) {
        cin>>n>>C;
        st.clear();
        for (int i = 0; i < n; ++i) {
            int cur = 0;
            cin>>cur; st.insert(cur);
        }
        int ans = 0;
        while (!st.empty()) {
            ++ans;
            set<int>::iterator it = st.end();
            --it;
            int val = *it; st.erase(it);
            if (st.empty()) break;
            set<int>::iterator bef = st.upper_bound(C - val);
            if (bef == st.begin()) continue;
            --bef;
            st.erase(bef);

        }
        printf("Case #%d: %d\n", ++cs, ans);
    }
    return 0;
}
