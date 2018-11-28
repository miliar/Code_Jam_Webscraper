#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define lx(x) (x<<1)
#define rx(x) (x<<1|1)
#define debug puts("here")
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define foreach(i,vec) for(unsigned i=0;i<vec.size();i++)
#define pb push_back
#define RD(n) scanf("%d",&n)
#define RD2(x,y) scanf("%d%d",&x,&y)
#define RD3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define RD4(x,y,z,w) scanf("%d%d%d%d",&x,&y,&z,&w)

/******** program ********************/

const int MAXN = 105;

int a[MAXN][MAXN],n,m;

bool check(int x,int y){
    bool ok = true;
    rep(i,n)
        if(a[i][y]>a[x][y])
            ok = false;
    if(ok)return true;

    rep(j,m)
        if(a[x][j]>a[x][y])
            return false;
    return true;
}

bool solve(){
    rep(i,n)
        rep(j,m)
            if(!check(i,j))
                return false;

    return true;
}

int main(){


	freopen("B-large.in","r",stdin);
	freopen("sum.out","w",stdout);


    int ncase;
    RD(ncase);
    rep1(Ncase,ncase){
        printf("Case #%d: ",Ncase);
        RD2(n,m);
        rep(i,n)
            rep(j,m)
                RD(a[i][j]);
        solve()?puts("YES"):puts("NO");
    }

	return 0;
}
