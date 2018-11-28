#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <map>
#include <vector>

using namespace std;

const int P = 1000002013;

int T, cas;

void run() {
    int n, m, x, y, z;
    scanf("%d%d", &n, &m);
    map<int, long long> cnt;
    long long total = 0;
    for (int i = 0; i < m; i++) {
        scanf("%d%d%d", &x, &y, &z);
        cnt[x] += z;
        cnt[y] -= z;
        long long dis = y - x;
        long long price = ((2*n-dis+1)*dis/2) % P;
        long long tt = price * z % P;
        total = (total + tt) % P;
    }
    vector<pair<int, long long> > cur;
    int sum = 0;
    long long ans = 0;
    for (map<int, long long>::iterator it = cnt.begin(); it != cnt.end(); it++) {
        if (it->second == 0)
            continue;
        if (it->second > 0)
            cur.push_back(make_pair(it->first, it->second));
        else {
            long long rem = -it->second;
            int pos = it->first;
            while (rem > 0) {
                long long c = min(cur.back().second, rem);
                rem -= c;
                cur.back().second -= c;
                int st = cur.back().first;
                if (cur.back().second == 0)
                    cur.pop_back();
                long long dis = it->first - st;
                long long price = ((2*n-dis+1)*dis/2) % P;
                long long total = price * c % P;
                ans = (ans + total) % P;
            }
        }
    }
    cout << "Case #" << cas << ": " << (total - ans + P) % P << endl;
}

int main() {
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++)
        run();
    return 0;
}
