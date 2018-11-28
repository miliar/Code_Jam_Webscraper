#include <bits/stdc++.h>
using namespace std;
const int N = 60, M = 2510;

int a[N * 2][N], id[N * 2], b[N][N], c[N], v[N * 2];
int n;

struct CMP{
    int now;
    CMP(int now) : now(now) {}
    bool operator () (int x, int y){
        return a[x][now] < a[y][now];
    }
};

// bool check_row(int now, int off){
//     for(int i = 0; i < now; ++i) if(a[id[off]][i] != b[now][i]) return false;
//     for(int i = now; i < n; ++i) if(now > 0 && a[id[off]][i] <= b[now - 1][i]) return false;
//     return true;
// }

// bool check_col(int now, int off){
//     for(int i = 0; i < now; ++i) if(a[id[off]][i] != b[i][now]) return false;
//     for(int i = now; i < n; ++i) if(now > 0 && a[id[off]][i] <= b[i][now - 1]) return false;
//     return true;
// }

// void put_row(int now, int off){
//     for(int i = now; i < n; ++i) b[now][i] = a[id[off]][i];
// }

// void put_col(int now, int off){
//     for(int i = now; i < n; ++i) b[i][now] = a[id[off]][i];
// }

// bool solve(int now, int off){
//     // puts("\n");
//     // for(int i = 0; i < n; ++i){
//     //     for(int j = 0; j < n; ++j){
//     //         printf("\t%d", i < now || j < now ? b[i][j] : -1);
//     //     }
//     //     puts("");
//     // }
//     // puts("");
//     sort(id + off, id + n * 2 - 1, CMP(now));
//     if(now == n - 1 || a[id[off]][now] != a[id[off + 1]][now]){
//         if(!check_col(now, off) && !check_row(now, off)) return false;
//         // printf("~~~%d %d\n", now, off);
//         int j;
//         for(j = 0; j < now; ++j) if(a[id[off]][j] != b[now][j]) break;
//         for(int i = 0; i < now; ++i){
//             if(j >= now) c[i] = b[i][now];
//             else c[i] = b[now][i];
//         }
//         memset(v + off, 0, sizeof(v[0]) * (2 * n - off + 5));
//         int k = now + 1;
//         for(j = off + 1; j < 2 * n - 1 && k < n; ++j){
//             if(a[id[j]][now] == a[id[off]][k]){
//                 v[j] = 1;
//                 ++k;
//             }
//         }
//         c[now] = a[id[off]][now];
//         for(j = off + 1, k = now + 1; j < 2 * n - 1; ++j) if(!v[j]) c[k++] = a[id[j]][now];
//         return true;
//     }
//     else{
//         if(check_col(now, off) && check_row(now, off + 1)){
//             put_col(now, off);
//             put_row(now, off + 1);
//             if(solve(now + 1, off + 2)) return true;
//         }
//         else if(check_col(now, off + 1) && check_row(now, off)){
//             put_col(now, off + 1);
//             put_row(now, off);
//             if(solve(now + 1, off + 2)) return true;
//         }
//         return false;
//     }
// }

int d[N][2];
void solve(){
    for(int i = 0; i < n * 2; ++i) id[i] = i;
    int u;
    for(int now = 0, off = 0; now < n; ++now){
        sort(id + off, id + n * 2 - 1, CMP(now));
        if(off + 1 == n * 2 - 1 || a[id[off]][now] != a[id[off + 1]][now]){
            u = now;
            d[now][0] = id[off++];
        }
        else{
            d[now][0] = id[off++];
            d[now][1] = id[off++];
        }
    }
    // cout << u << endl;
    // for(int i = 0; i <n; ++i) cout << d[i][0] << ' ' << d[i][1] << endl;
    for(int i = 0; i < n; ++i){
        if(i == u) c[i] = a[d[i][0]][u];
        else{
            if(a[d[i][0]][u] != a[d[u][0]][i]) c[i] = a[d[i][0]][u];
            else c[i] = a[d[i][1]][u];
        }
    }
}

int main(){
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        scanf("%d", &n);
        for(int i = 0; i < 2 * n - 1; ++i){
            for(int j = 0; j < n; ++j) scanf("%d", &a[i][j]);
        }
        solve();
        printf("Case #%d:", cas);
        for(int i = 0; i < n; ++i) printf(" %d", c[i]);
        puts("");
    }
    return 0;
}