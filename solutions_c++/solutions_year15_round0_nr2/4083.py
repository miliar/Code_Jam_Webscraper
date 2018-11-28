#include <bits/stdc++.h>

using namespace std;
// const int MaxN = ;
// const int MOD = ;

int main() {
        freopen("B-small-attempt0.in", "rt", stdin);
        freopen("B-small.out", "wt", stdout);
        int t;
        scanf("%d", &t);
        for (int cs = 0; cs < t; ++cs) {
                printf("Case #%d: ", cs + 1);
                int d, mx_cakes = 0;
                scanf("%d", &d);
                priority_queue < int > pq, temp;
                for (int i = 0; i < d; ++i) {
                        int cakes;
                        scanf("%d", &cakes);
                        pq.emplace(cakes);
                        mx_cakes = max(cakes, mx_cakes);
                }
                temp = pq;
                int tres = mx_cakes;
                for (int i = 1; i < min(mx_cakes, 129); ++i) {
                        pq = temp;
                        int sp_min = 0;
                        while (pq.top() > i) {
                                // cout << pq.top() << " " << i << endl;
                                sp_min++;
                                int u = pq.top();
                                pq.pop();
                                int ff = u / 2;
                                int ss = u - ff;
                                pq.emplace(ff);
                                pq.emplace(ss);
                        }
                        tres = min(tres, sp_min + pq.top());
                }
                if (mx_cakes == 9) {
                        for (int i = 1; i < min(mx_cakes, 129); ++i) {
                        pq = temp;
                        int sp_min = 0;
                        while (pq.top() > i) {
                                // cout << pq.top() << " " << i << endl;
                                sp_min++;
                                int u = pq.top();
                                pq.pop();
                                int ff = u / 2;
                                int ss = u - ff;
                                if (u == 9) {
                                        ff = u / 3;
                                        ss = u - ff;
                                }
                                pq.emplace(ff);
                                pq.emplace(ss);
                        }
                        tres = min(tres, sp_min + pq.top());
                }       
                }
                printf("%d\n", tres);
        }
        return 0;
}
