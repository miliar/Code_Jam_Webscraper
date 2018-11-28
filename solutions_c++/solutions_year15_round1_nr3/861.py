#include <iostream>
#include <vector>


/* PROBLEM 3 */


using namespace std;


int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int qq = 1; qq <= T; qq++) {
        printf("Case #%d:\n", qq);
        
        int N;
        scanf("%d", &N);
        
        
        vector< pair<long long, long long> >points;
        long long m, n;
        
        for (int i = 0; i < N; i++) {
            scanf("%lld%lld", &m, &n);
            points.push_back(make_pair(m, n));
        }
        
        
        if (N <= 3) {
            for (int i = 0; i < N; i++) {
                int n = 0;
                printf("%d\n", n);
            }
            continue;
        }
        
        for (int i = 0; i < points.size(); i++) {
            long long minimum = 100000000;
            int above, below;
            pair<long, long>a = points[i];
            for (int j = 0; j < points.size(); j++) {
                above = below = 0;
                if (i == j) continue;
                pair<long, long>b = points[j];
                for (int k = 0; k < points.size(); k++) {
                    if (k == i || k == j) continue;
                    pair<int, int>c = points[k];
                    long long dot = (b.first - a.first) * (c.second - a.second) - (b.second - a.second) * (c.first - a.first);
                    if (dot < 0) {
                        above++;
                    } else if (dot > 0) {
                        below++;
                    }
                }
                long long sub_minimum = min(above, below);
                minimum = min(minimum, sub_minimum);
            }
            printf("%lld\n", minimum);
        }
    }
    
    return 0;
}
