#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

set<int> st;

void insert(int x) {
    while (x) {
        st.insert(x % 10);
        x /= 10;
    }
}

int solve(int n) {
    int cur = n;
    st.clear();
    while (true) {
        insert(cur);
        if (st.size() == 10) break;
        cur += n;
    }
    return cur;
}

int main()
{
    //freopen("a.in", "r", stdin);
    //freopen("a_output.txt", "w", stdout);

    int n, cas = 0, t;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        if (n == 0) printf("Case #%d: INSOMNIA\n", ++cas);
        else printf("Case #%d: %d\n", ++cas, solve(n));
    }

    return 0;
}
