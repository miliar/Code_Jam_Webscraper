#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>

using namespace std;
int n, m;
multiset<int>S;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T = 0, CAS = 0;
    scanf("%d", &T);
    while(T--) {
        S.clear();
        scanf("%d%d", &n, &m);
        for(int i = 1; i <= n; i++) {
            int t;
            scanf("%d", &t);
            S.insert(t);
        }
        int cnt = 0;
        multiset<int>::iterator it;
        
        while(!S.empty()) {
            cnt++;
            it = S.end();
            it--;
            int now = *it;
            int need = m - now;
            S.erase(it);
            it = upper_bound(S.begin(), S.end(), need);
            if(it == S.begin()) {
                //continue;
            } else {
                it--;
                now = *it;
                S.erase(it);
            }
        }
        printf("Case #%d: %d\n",++CAS, cnt);

    }
}