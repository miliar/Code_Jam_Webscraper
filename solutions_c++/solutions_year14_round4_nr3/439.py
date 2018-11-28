#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <bitset>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#define dou double
#define mem(a) memset(a, 0, sizeof(a))
#define memm(a) memset(a, -1, sizeof(a))
#define LL long long
#define PB push_back
#define MP make_pair
#define PII pair<int, int>
#define FI first
#define SE second
#define RI(a) scanf("%d", &(a))
#define RII(a, b) scanf("%d%d", &(a), &(b))
#define RIII(a, b, c) scanf("%d%d%d", &(a), &(b), &(c))
#define RL(a) scanf("%lld", &(a))
#define RLL(a, b) scanf("%lld%lld", &(a), &(b))
#define RLLL(a, b, c) scanf("%lld%lld%lld", &(a), &(b), &(c)) 
#define PI(r) printf("%d\n", (r))
#define PL(r) printf("%lld\n", (r))
#define RS(s) scanf("%s", (s))
#define SL(a) strlen(a)
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define REPP(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FOR(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
//Segment tree
#define MID ((l + r) >> 1)
#define L (x << 1)
#define R ((x << 1) | 1)
#define LC L, l, MID
#define RC R, MID + 1, r
#define LB(x) ((x) & (-(x)))
#pragma warning (disable : 4996)
//#pragma comment(linker, "/STACK:102400000,102400000")
#define EPS 1e-8
#define INF 2000000000
#define LIM (1ll << 60)
#define MOD 1000000007
#define N 555

using namespace std;

struct  Edge {
    int v , w , next;
}e[N * N * 4];

int dx[4] = {0, 0, -1, 1}, dy[4] = {1, -1, 0, 0};
int st , en , cur[N * N] , lvl[N * N];
int w , h , k , a[N][N];
int head[N * N] , tot;

void addinv (int u , int v , int w) {
    e[tot].v = v;e[tot].w = w;e[tot].next = head[u];head[u] = tot ++;
}

void add (int u , int v , int w) {
    addinv (u , v , w);
    addinv (v , u , 0);
}

bool bfs(){
    queue<int> q;
    memm(lvl);
    lvl[st] = 0;
    q.push(st);
    while(! q.empty()){
        int u = q.front();q.pop();
        for(int i = head[u];i != -1;i = e[i].next){
            int v = e[i].v;
            if(e[i].w && lvl[v] == -1){
                lvl[v] = lvl[u] + 1;
                q.push(v);
            }
        }
    }
    return lvl[en] != -1;
}

int dfs(int u,int flow){
    if(u == en) return flow;
    int tmp = flow;
    for(int &i = cur[u];i != -1;i = e[i].next){
        int v = e[i].v;
        if(e[i].w && lvl[v] == lvl[u] + 1){
            int add = dfs(v,min(e[i].w,tmp));
            tmp -= add;
            e[i].w -= add;
            e[i ^ 1].w += add;
            if(! tmp) break;
        }
    }
    return flow - tmp;
}


int Dinic(){
    int ma = 0;
    while(bfs()){
        for(int i = 0;i < N * N ;i ++)
            cur[i] = head[i];
        ma += dfs(st,int(1e9));
    }
    return ma;
}

int main(){
    int t, x, y, z, ca = 1;
    freopen("D:/Contest/1.in", "r", stdin);
    freopen("1.ans", "w", stdout);
    //ios :: sync_with_stdio(false);

    RI(t);
    while (t --) {
        tot = 0;
        memm(head);
        RIII(w, h, k);
        mem(a), mem(cur);
        REP(i, k) {
            int lx , rx , ly , ry;
            scanf ("%d %d %d %d" , &lx , &ly , &rx , &ry);
            for (int x = lx ; x <= rx ; x ++) {
                for (int y = ly ; y <= ry ; y ++)
                    a[x][y] = 1;
            }
        }
        st = N * N - 1;
        en = N * N - 2;
        int lef = w * h + 5;
        REP(i, w) {
            add (st , i * h , 1);
            add (i * h + h - 1 , en , 1);
        }
        REP(i, w) REP(j, h){
            if (a[i][j]) continue;
            add (i * h + j , lef + i * h + j , 1);
            REP(r, 4) {
                int x = i + dx[r] , y = j + dy[r];
                if (x >= 0 && x < w && y >= 0 && y < h && !a[i][j] && !a[x][y]) {
                    add (lef + i * h + j , x * h + y , 1);
                }
            }
        }
        printf ("Case #%d: %d\n" , ca++ , Dinic());
    }

    return 0;
}