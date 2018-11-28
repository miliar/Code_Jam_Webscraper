#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

#define MOD 1000002013
#define MAX_M 1000

#define SEG_COUNT(x) (x).second.second
#define SEG_START(x) (x).first
#define SEG_END(x) (x).second.first

typedef pair<long long, pair<long long, long long> > Seg;
vector<Seg> segs;

vector<pair<long long, long long> > s;
vector<pair<long long, long long> > exits;

int N, M;

long long price(long long dist) {
    if (dist == 0) return 0;
    long long first = N;
    long long last = N - dist + 1;
    return ((first + last) * dist / 2) % MOD;
}

long long solve() {
    sort(segs.begin(), segs.end());
    sort(exits.begin(), exits.end());

    long long org_sum = 0;
    for (int i = 0; i < M; i++) {
        int local_sum = price(SEG_END(segs[i]) - SEG_START(segs[i])) * SEG_COUNT(segs[i]) % MOD;
        org_sum += local_sum;
        org_sum %= MOD;
    }
//cout << org_sum << endl;

    long long sum = 0;
    s.clear();
    for (int i = 0; i < exits.size(); i++) {
//cout << exits[i].first << ' ' << exits[i].second << endl;
        if (exits[i].second < 0) {
            s.push_back(make_pair(exits[i].first, 0-exits[i].second));
        } else {
            int people = exits[i].second;
            for (int j = s.size() - 1; j >= 0; j--) {
                if (people > s[j].second) {
                    sum += price(exits[i].first - s[j].first) * s[j].second;
                    sum %= MOD;
                    people -= s[j].second;
                    s.pop_back();
                } else {
                    sum += price(exits[i].first - s[j].first) * people;
                    sum %= MOD;
                    s[j].second -= people;
                    break;
                }
            }
        }
    }
//cout << sum << endl;

    return (org_sum + MOD - sum) % MOD;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++) {
        scanf("%d%d", &N, &M);
        segs.clear();
        exits.clear();
        for (int i = 0; i < M; i++) {
            int s, e, c;
            scanf("%d%d%d", &s, &e, &c);
            segs.push_back(make_pair(s, make_pair(e, c)));

            exits.push_back(make_pair(s, 0-c));
            exits.push_back(make_pair(e, c));
        }
        
        printf("Case #%d: %lld\n", testcase, solve());
    }
    return 0;
}
