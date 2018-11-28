#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>

using namespace std;

const long long kPrime = 1000002013, kMaxPairs = 1000 + 100;

int numStops, numPairs, s[kMaxPairs], t[kMaxPairs], cnt[kMaxPairs];

pair<int, int> l[kMaxPairs * 2];

bool lComp(const pair<int, int>& a, const pair<int, int>& b) {
   return a.first != b.first ? a.first < b.first : a.second > b.second;
}

void add(long long* result, long long val, int cnt) {
    val = (val % kPrime) * cnt;
    *result += val % kPrime;
    if (*result >= kPrime)
        *result %= kPrime;
}

long long calcRev(long long dis) {
    return numStops * dis - (0 + dis - 1) * dis / 2;
}

void solve() {
    long long expRev = 0, actRev = 0;
    for (int i = 0; i < numPairs; ++i) {
        l[i * 2] = make_pair(s[i], cnt[i]);
        l[i * 2 + 1] = make_pair(t[i], -cnt[i]);
        add(&expRev, calcRev(t[i] - s[i]), cnt[i]);
    }
    sort(l, l + numPairs * 2, lComp);
    vector<pair<int, int> > st;
    for (int i = 0; i < numPairs * 2; ++i) {
        int cPos = l[i].first, cCnt = l[i].second;
        if (cCnt > 0) {
            st.push_back(make_pair(cPos, cCnt));
        } else {
            cCnt *= -1;
            while (cCnt > 0) {
                assert(st.size() > 0);
                int s0 = st[st.size() - 1].first,
                    t0 = cPos,
                    c0 = min(st[st.size() - 1].second, cCnt);
                cCnt -= c0;
                st[st.size() - 1].second -= c0;
                if (st[st.size() - 1].second == 0)
                    st.pop_back();
                add(&actRev, calcRev(t0 - s0), c0);
            }
        }
    }
    // cerr << endl << expRev << " " << actRev << endl;
    long long lostRev = (expRev + kPrime - actRev) % kPrime;
    printf("%d", (int)lostRev);
}

int main() {
    int numCases;
    scanf("%d", &numCases);
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        scanf("%d %d", &numStops, &numPairs);
        for (int i = 0; i < numPairs; ++i)
            scanf("%d %d %d", &s[i], &t[i], &cnt[i]);

        printf("Case #%d: ", caseNo);
        solve();
        printf("\n");
    }
    return 0;
}
