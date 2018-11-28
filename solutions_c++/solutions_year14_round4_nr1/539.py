#include <cstdio>
#include <set>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        int n, x, t;
        scanf("%d %d", &n, &x);

        multiset<int> s;
        for (int i = 0; i < n; i++) {
            int tmp;
            scanf("%d", &tmp);
            s.insert(tmp);
        }

        int ans = 0;
        while (!s.empty()) {
            ans++;

            multiset<int>::iterator biggest = s.end();
            int biggest_val = *(--biggest);
            s.erase(s.lower_bound(biggest_val));

            multiset<int>::iterator cur = s.upper_bound(x - biggest_val);
            if (cur == s.begin())
                continue;
            s.erase(--cur);
        }

        printf("Case #%d: %d\n", z, ans);
    }
}
