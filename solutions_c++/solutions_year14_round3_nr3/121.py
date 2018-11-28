#include <iostream>
#include <queue>
#include <stdio.h>
#include <string.h>

using namespace std;

int T, v[30], N, M, K, di[4] = {0, 0, -1, 1}, dj[4] = {-1, 1, 0, 0}, caseNumber = 1;
int to(int i, int j) {
    return i * M + j;
}
pair<int, int> from(int x) {
    return {x / M, x % M};
}
int count(int x) {
    int ret = 0;
    while(x > 0) {
        ret += x & 1;
        x >>= 1;
    }

    return ret;
}
int main() {
    freopen("enclose.in", "r", stdin);    
    freopen("enclose.out", "w", stdout);    
    cin >> T;
    while(T-- > 0) {
        cin >> N >> M >> K;
        //for(int N = 1; N <= 20; N++)
        //for(int M = 1; M <= 20; M++) 
        //for(int K = 1; K <= N * M; K++) {


        int area = N * M;
        if (area > 20) continue;
        int ans = area;
        for(int m = 0; m < 1 << area; m++) {
            queue<int> q;
            memset(v, 0, sizeof(v));

            for(int i = 0; i < N; i++) {
                if ((m & (1 << to(i, 0))) == 0) {v[to(i, 0)] = 1; q.push(to(i, 0));}
                if ((m & (1 << (to(i, M - 1)))) == 0) {v[to(i, M - 1)] = 1; q.push(to(i, M - 1));}
            }
            for(int j = 0; j < M; j++) {
                if ((m & (1 << to(0, j))) == 0) {v[to(0, j)] = 1; q.push(to(0, j));}
                if ((m & (1 << (to(N - 1, j)))) == 0) {v[to(N - 1, j)] = 1; q.push(to(N - 1, j));}
            }

            while(q.size() > 0) {
                int x = q.front(); q.pop();
                pair<int, int> p = from(x);
                for(int d = 0; d < 4; d++) {
                    int ii = p.first + di[d];
                    int jj = p.second + dj[d];

                    if (ii < 0 || ii >= N || jj < 0 || jj >= M) continue;
                    if ((m & (1 << to(ii, jj))) != 0) continue;
                    if (v[to(ii, jj)]) continue;
                    
                    v[to(ii, jj)] = 1;
                    q.push(to(ii, jj));
                }
            }

            int ret = 0;
            for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++) if (!v[to(i, j)]) ret++;

            if (ret >= K) {
                ans = min(ans, count(m));
            }
        }
        
        //printf("%d %d %d %d\n", N, M, K, ans);
        printf("Case #%d: %d\n", caseNumber++, ans);
    }
    return 0;
}
