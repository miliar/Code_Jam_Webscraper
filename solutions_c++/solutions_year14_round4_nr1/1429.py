#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int T, N, C;
vector<int> V;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for ( int t = 1; t <= T; t++ ) {
        V.clear();
        scanf("%d%d", &N, &C);
        for ( int i = 0; i < N; i++ ) {
            int A;
            scanf("%d", &A);
            V.push_back(A);
        }
        sort(V.begin(), V.end(), greater<int>());
        int cnt = V.size() - 1;
        int ans = 0;
        for ( int i = 0; i <= cnt; i++ ) {
            if ( V[i] + V[cnt] > C ) ans++;
            else {
                ans++;
                cnt--;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
