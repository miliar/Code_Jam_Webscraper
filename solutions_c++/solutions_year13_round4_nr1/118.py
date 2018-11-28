#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <queue>
#include <algorithm>

#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)

const int MOD = 1000002013;

int n, m;

std::vector <std::pair <int, int> > events;

int cost(int s, int e) {
    int k = e - s;
    if (k) {
        return (long long)(n + n - k + 1) * k / 2 % MOD;
    }
    return 0;
}

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        scanf("%d%d", &n, &m);
        events.clear();
        int answer = 0;
        for (int i = 0; i < m; ++ i) {
            int s, e, p;
            scanf("%d%d%d", &s, &e, &p);
            (answer += (long long)cost(s, e) * p % MOD) %= MOD;
            events.push_back(std::make_pair(s, -p));
            events.push_back(std::make_pair(e, p));
        }
        std::sort(events.begin(), events.end());
        std::priority_queue <std::pair <int, int> > tickets;
        foreach (iter, events) {
            if (iter->second < 0) {
                tickets.push(std::make_pair(iter->first, -iter->second));
            } else {
                int need = iter->second;
                while (need) {
                    std::pair <int, int> ret = tickets.top();
                    tickets.pop();
                    int tmp = std::min(ret.second, need);
                    ret.second -= tmp;
                    if (ret.second) {
                        tickets.push(ret);
                    }
                    need -= tmp;
                    (answer -= (long long)cost(ret.first, iter->first) * tmp % MOD) %= MOD;
                }
            }
        }
        printf("Case #%d: %d\n", t, (answer + MOD) % MOD);
    }
    return 0;
}
