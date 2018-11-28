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

int a[1005];

bool ok(int n){
    int id[10],top = 0;
    while(n){
        id[++top] = n%10;
        n /= 10;
    }
    for(int i=1;i<=top;i++)
        if(id[i]!=id[top--])
            return false;
    return true;
}

int cal(int n){
    return ok(n)&&ok(n*n);
}

int main(){

	freopen("C-small-attempt0.in","r",stdin);
	freopen("sum.out","w",stdout);

    for(int i=1;i*i<=1000;i++)
        if(cal(i))
            a[i*i] = 1;
    rep1(i,1000)
        a[i] += a[i-1];
    int ncase;
    RD(ncase);
    rep1(Ncase,ncase){
        printf("Case #%d: ",Ncase);
        int n,m;
        RD2(n,m);
        cout<<a[m]-a[n-1]<<endl;
    }

	return 0;
}
