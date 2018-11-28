#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <queue>
using namespace std;

int bfs(string st)
{
    queue<string> q;
    unordered_map<string, int> f;
    unordered_set<string> mark;
    q.push(st);

    for (int i = 0; i < st.size(); ++ i) {
        st[i] = '+';
    }

    while (q.size()) {
        string s = q.front();
        q.pop();
        mark.erase(s);
        int cur = f[s];
        if (f.count(st) && cur >= f[st]) {
            continue;
        }

        int ptr = s.size() - 1;
        while (ptr >= 0 && s[ptr] == '+') {
            -- ptr;
        }


        for (int i = 0; i <= ptr; ++ i) {
            string t = s;
            for (int j = 0; j <= i; ++ j) {
                t[j] = s[i - j] == '+' ? '-' : '+';
            }
            if (!f.count(t) || f[t] > cur + 1) {
                f[t] = cur + 1;
                if (!mark.count(t)) {
                    mark.insert(t);
                    q.push(t);
                }
            }
        }
    }


    return f[st];
}

int solve()
{
    char s[100 + 1];
    scanf("%s", s);
    return bfs(s);
}

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        printf("Case #%d: %d\n", test, solve());
    }
    return 0;
}
