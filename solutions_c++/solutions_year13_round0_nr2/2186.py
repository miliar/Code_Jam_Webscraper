#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <cmath>
#include <list>
#include <vector>
#include <iomanip>
#include <cctype>
#include <complex>
#include <iterator>
#include <ostream>
#include <bitset>
#define all(a) a.begin(),a.end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define clx complex<long double>
typedef long long ll;
typedef long double ldb;
typedef unsigned long long ull;

using namespace std;
int _bufint;
inline int in(){
    scanf("%d", &_bufint);
    return _bufint;
}
const ll LINF=~((1ll)<<63);
const int INF=~(1<<31);
struct pl{
    ll x,y,z;
    ll dx,dy,dz;
    ll nx, ny, nz;
    ll left, right;
    pl(int xx, int yy, int zz, int dxx, int dyy, int dzz){
        x=xx;
        y=yy;
        z=zz;
        dx=dxx;
        dy=dyy;
        dz=dzz;
        nx=x;
        ny=y;
        nz=z;
        left=-1, right=-1;
    }
    void step(int n){
        nx=x+dx*n;
        ny=y+dy*n;
        nz=z+dz*n;
    }
    ull dist(){
        return (ull)(nx*nx)+ull(ny*ny)+ull(nz*nz);
    }
};
/*
struct node{
    vector<int> cur;
    node(int a){
        cur.pb(a);
    }
    node(){
    }
};
const int maxn=1000000*4+100;
node tree[maxn];
node merge(node a, node b){
    node c;
    c.cur.assign(a.cur.size()+b.cur.size(),0);
    merge(a.cur.begin(), a.cur.end(), b.cur.begin(), b.cur.end(), c.cur.begin());
    return c;
}
int query(int v, int tl, int tr, int l, int r, int cr){
    if(l>r) return 0;
    if(tr==r && tl==l){
        return (upper_bound(tree[v].cur.begin(), tree[v].cur.end(), cr) - tree[v].cur.begin() - 1);
    }
    int tm=tl+(tr-tl)/2;
    return query(2*v, tl, tm, l, min(r, tm), cr) + query(2*v+1, tm+1, tr, max(l, tm+1), r, cr);
}
*/
int main(){
#ifdef SSU
    freopen("input12.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    srand(time(0));

    int T=in();
    for(int t=1;t<=T;++t){
        int n=in(), m=in();
        vector<vector<int> > g(n, vector<int>(m,0));
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                g[i][j]=in();
            }
        }
        bool res=1;
        for(int i=0;i<n;++i){
            if(!res) break;
            for(int j=0;j<m;++j){
                bool r=1;
                for(int k=0;k<n;++k){
                    if(g[k][j]>g[i][j]){
                        r=0;
                        break;
                    }
                }
                if(r){
                    continue;
                }

                r=1;
                for(int k=0;k<m;++k){
                    if(g[i][k]>g[i][j]){
                        r=0;
                        break;
                    }
                }
                if(r){
                    continue;
                }

                res=0;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(res) puts("YES");
        else puts("NO");

    }



    return 0;
}
