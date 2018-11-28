#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
#define N 2005
const LL Mod = 1000002013;
struct E{
    LL l, r, p;
} e[N];

LL in[N], out[N], pos[N];
int q[N];
int main(){
    freopen("1.txt","r",stdin);
    freopen("1.out","w",stdout);
    LL n;
    int tt, m, i, cnt, cal=0;
    LL dis, cc;
    scanf("%d",&tt);
    while(tt--){
        memset(in,0,sizeof(in));
        memset(out,0,sizeof(out));
        cc = 0;
        cnt = 0;
        cin >> n >> m;
       // scanf("%d%d",&n,&m);
        for(i=1;i<=m;++i){
            cin >> e[i].l >> e[i].r >> e[i].p;
           // scanf("%d%d%d",&e[i].l,&e[i].r,&e[i].p);
            dis = e[i].r - e[i].l;
            cc = (cc + (((2*n-dis+1)*dis/2)%Mod*e[i].p)%Mod)%Mod;
            pos[cnt++] = e[i].l;
            pos[cnt++] = e[i].r;
        }
        sort(pos,pos+cnt);
        cnt = unique(pos,pos+cnt) - pos;
        for(i=1;i<=m;++i){
            int x = lower_bound(pos,pos+cnt,e[i].l) - pos;
            int y = lower_bound(pos,pos+cnt,e[i].r) - pos;
            in[x] += e[i].p;
            out[y] += e[i].p;
        }
        int top = 0;
        LL cost = 0, del;
        for(i=0;i<cnt;++i){
            if(in[i]) q[++top] = i;
            LL tot = out[i];
            while(top && tot){
                if(tot>=in[q[top]]){
                    tot -= in[q[top]];
                    del = in[q[top]];
                    dis = pos[i]-pos[q[top]];
                    --top;
                }else{
                    del = tot;
                    in[q[top]] -= tot;
                    dis = pos[i]-pos[q[top]];
                    tot = 0;
                }
                cost = (cost + (((2*n-dis+1)*dis/2)%Mod * del)%Mod)%Mod;
            }
        }
        printf("Case #%d: ", ++cal);
        cout << (cc - cost+Mod)%Mod << endl;
    }
    return 0;
}
