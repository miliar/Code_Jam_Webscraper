#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

const int N = 100010;;
const int inf = ~0U >> 3;

struct node{int to,next,c;}e[N*8];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int box[N], size;
int mp[510][510];
int n, m, k;
int tot, start, end;
int h[N],vh[N];

void add(int from,int to,int c)
{
    e[size].to=to;
    e[size].c=c;
    e[size].next=box[from];
    box[from]=size++;
    e[size].to=from;
    e[size].c=0;
    e[size].next=box[to];
    box[to]=size++;
}
int id(int i, int j){
    return i * m + j;
}
int in(int x){
    return x;
}
int out(int x){
    return x + n * m;
}
bool in_range(int x, int y){
    return x >= 0 && x < n && y >= 0 && y < m;
}
int aug(int x,int c)
{
    if(x==end)return c;
    int tem=h[x]+1,l=c;
    for(int i=box[x];~i;i=e[i].next)
    if(e[i].c && h[e[i].to]+1==h[x])
    {
        int d=aug(e[i].to,min(e[i].c,l));
        e[i].c-=d,e[i^1].c+=d,l-=d;
        if(!l || h[start]==tot)return c-l;
    }
    for(int i=box[x];~i;i=e[i].next)
    if(e[i].c)tem=min(tem,h[e[i].to]);
    if(!--vh[h[x]])h[start]=tot;else ++vh[h[x]=tem+1];
    return c-l;
}
int SAP()
{
    int s=0;
    memset(h,0,sizeof(h));
    memset(vh,0,sizeof(vh));
    vh[0]=tot;
    while(h[start]<tot)s+=aug(start,~0U>>1);
    return s;
}
int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int _, cas = 1;
    for(scanf("%d", &_); _--; ){
        printf("Case #%d: ", cas++);
        scanf("%d %d %d", &m, &n, &k);
        memset(mp, 0, sizeof(mp));
        for(int i = 0, x1, y1, x2, y2; i < k; ++i){
            scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
            for(int x = x1; x <= x2; ++x)
                for(int y = y1; y <= y2; ++y)
                    mp[x][y] = 1;
        }
//        for(int i= 0; i < n; ++i, cout << endl)
//            for(int j = 0; j < m; ++j) cout << mp[i][j]; cout << endl;
        memset(box, -1, sizeof(box)), size = 0;
        tot = n * m * 2 + 2, start = tot - 2, end = tot - 1;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j){
                if(mp[i][j]) continue;
                if(i == 0) add(start, in(id(i, j)), inf);
                if(i == n - 1) add(out(id(i, j)), end, inf);
                add(in(id(i, j)), out(id(i, j)), 1);
                for(int k = 0; k < 4; ++k){
                    int ii = i + dx[k], jj = j + dy[k];
                    if(in_range(ii, jj) && mp[ii][jj] == 0) add(out(id(i, j)), in(id(ii, jj)), inf);
                }
            }
        cout << SAP() << endl;
    }
    return 0;
}
