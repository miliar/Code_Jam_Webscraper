#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int w, h, b;
int x0[1024], y00[1024], x1[1024], y11[1024];
int a[1024][1024];
int d[1024];

priority_queue< pair<int, int> > pq;

void read() {
    scanf("%d%d%d", &w, &h, &b);
    
    for (int i = 1; i <= b; i++) {
        scanf("%d%d%d%d", &y00[i], &x0[i], &y11[i], &x1[i]);
    }
}

int get(int x0, int x1, int y0, int y1) {
    if (x0 <= y1 && y0 <= x1) return 0;
    return min(abs(x1 - y0), abs(y1 - x0));
}

void solve() {
    int n = b;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            a[i][j] = max(get(x0[i], x1[i], x0[j], x1[j]),  get(y00[i], y11[i], y00[j], y11[j]));
            
            if (a[i][j]) -- a[i][j];
        }
    }
    
    while (!pq.empty()) pq.pop();
    int ans = w;
    
    for (int i = 1; i <= n; i++) {
        pq.push(make_pair(-y00[i], i));
        d[i] = y00[i];
    }
    while (!pq.empty()) {
        int c = -pq.top().first;
        int x = pq.top().second;
        pq.pop();
        
        if (d[x] < c) continue;
        
   //     printf ("%d %d   %d\n", x, c, y11[x]);
        
        ans = min(ans, w - y11[x] - 1 + c);
        
        for (int i = 1; i <= n; i++) {
            if (c + a[x][i] < d[i]) {
                d[i] = c + a[x][i];
                pq.push(make_pair(-d[i], i));
            }
        }
    }
    
    printf ("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
