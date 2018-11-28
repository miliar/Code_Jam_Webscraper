#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;
typedef long long LL;
#define N 505
#define M 1000005
int ca;
int W , H , B;
bool g[N][N];

int n , m , s , t;
struct arc
{
    int x , f , next;
}e[M << 2];
int pre[M] , mcnt;
void addarc(int x ,int y ,int z)
{
    e[mcnt] = (arc) {y , z , pre[x]} , pre[x] = mcnt ++;
    e[mcnt] = (arc) {x , 0 , pre[y]} , pre[y] = mcnt ++;
}
int d[M] , cur[M] , q[M];
bool BFS()
{
    memset(d , -1 , sizeof(d));
    int top = 0 , bot = -1;
    q[++ bot] = s , d[s] = 1;
    while (top != bot + 1) {
        int x = q[top ++];
        for (int i = pre[x] ; ~i ;i = e[i].next) {
            int y = e[i].x;
            if (!~d[y] && e[i].f) {
                d[y] = d[x] + 1 , q[++ bot] = y;
                if (y == t) return 1;
            }
        }
    }
    return 0;
}
int DFS(int x , int flow = 1 << 30)
{
    if (x == t || !flow) return flow;
    int sum = 0 , u;
    for (int& i = cur[x] ; ~i ; i = e[i].next) {
        int y = e[i].x;
        if (d[y] == d[x] + 1 && (u = DFS(y , min(flow , e[i].f)))) {
            e[i].f -= u ,  e[i ^ 1].f += u;
            sum += u , flow -= u;
            if (!flow) break;
        }
    }
    if (!sum) d[x] = -1;
    return sum;
}

int dinic()
{
    int ans = 0;
    while (BFS()) {
        memcpy(cur , pre , sizeof(cur));
        ans += DFS(s);
    }
    return ans;
}
int id[N][N];
int dx[] = {0 , 1 , 0 , -1};
int dy[] = {1 , 0 , -1 , 0};

void work() {
    printf("Case #%d: " , ++ ca);
    int i , j , k , x , y , a , b;
    scanf("%d%d%d",&W,&H,&B);
    memset(g , 0 , sizeof(g));
    while (B --) {
        scanf("%d%d%d%d",&x,&y,&a,&b);
        for (i = x ; i <= a ; ++ i)
            for (j = y ; j <= b ; ++ j)
                g[j][i] = 1;
    }
    memset(pre , -1 , sizeof(pre));
    mcnt = 0;
    int num = 0;
    for (i = 0 ; i < H ; ++ i)
        for (j = 0 ; j < W ; ++ j)
            id[i][j] = num ++;
    for (i = 0 ; i < H ; ++ i) {
        for (j = 0 ; j < W ; ++ j) {
            for (k = 0 ; k < 4 ; ++ k) {
                x = i + dx[k] , y = j + dy[k];
                if (x >= 0 && x < H && y >= 0 && y < W) {
                    addarc(id[i][j] + num , id[x][y] , 1 << 30);
                }
            }
            if (!g[i][j])
                addarc(id[i][j] , id[i][j] + num , 1);
        }
    }
    s = num + num , t = s + 1;
    for (i = 0 ; i < W ; ++ i)
        addarc(s , id[0][i] , 1 << 30) , addarc(id[H - 1][i] + num , t , 1 << 30);
    printf("%d\n" , dinic());
}

int main()
{
    freopen("~input.txt" , "r" , stdin);
    freopen("~output.txt" , "w" , stdout);
    int _; scanf("%d",&_); while (_ --)
        work();
    return 0;
}
