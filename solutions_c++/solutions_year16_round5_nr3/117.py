#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;

int a[1000];
vector<char> b;
int n,m;
int f[1000000][3];
int x[2000],y[2000],z[2000],vx[2000],vy[2000],vz[2000];
vector<pair<double,pair<int,int> > > g;
const int inf =100000000;
int fa[2000];
stack<char> st;
int findfa(int t){
    int i=t;
    while (fa[i]!=0) i=fa[i];
    if (fa[t]!=0){
        int j=t;
        while (fa[j]!=i){
            int k=fa[j];
            fa[j]=i;
            j=k;
        }
    }
    return i;
}
void MAIN(){
    int s,t;
    cin >> n >> s;
    rep(i,n) cin >>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
    g.clear();
    rep(i,n) rep(j,n) g.pb(mp(sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+(z[i]-z[j])*(z[i]-z[j])),mp(i,j)));
    sort(g.begin(),g.end());
    rep(i,n) fa[i]=0;
    for(auto tmp:g){
        int xx=findfa(tmp.second.first),yy=findfa(tmp.second.second);
        if (xx!=yy){
            fa[xx]=yy;
            if (findfa(1)==findfa(2)) {
                //printf("%.6lf\n", tmp.first);
                cout << tmp.first <<endl;
                return;
            }
        }
    }
}

int main() {
    freopen("d:\\oi\\gcjr3\\C-small-attempt0.in","r",stdin);
    freopen("d:\\oi\\gcjr3\\C-small-attempt0.out","w",stdout);
    int tt;
    cin >> tt;
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }
    return 0;
}