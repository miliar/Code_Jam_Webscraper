#include <cstdio>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        int m, n;
        scanf("%d %d", &m, &n);

        vector<string> v;
        for (int i = 0; i < m; i++) {
            string str;
            cin >> str;
            v.push_back(str);
        }

        int cnt = 0;
        int ans = 0;

        for (int i = 0; i < 1<<(2*m); i++) {
            int mask = i;
            int maxserver = 0;
            set<string> servers[4];

            for (int j = 0; j < m; j++) {
                int server = mask & 3;
                maxserver = max(maxserver, server);
                mask >>= 2;

                for (int k = 0; k <= v[j].size(); k++)
                    servers[server].insert(v[j].substr(0, k));
            }

            if (maxserver < n) {
                int cur_ans = 0;
                for (int i = 0; i < n; i++)
                    cur_ans += servers[i].size();

                if (cur_ans > ans) {
                    ans = cur_ans;
                    cnt = 0;
                }

                if (ans == cur_ans)
                    cnt++;
            }
        }

        printf("Case #%d: %d %d\n", z, ans, cnt);
    }
}
