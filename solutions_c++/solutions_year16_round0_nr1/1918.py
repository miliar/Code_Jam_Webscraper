#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int go(int n){
    if(n==0) return -1;
    set<int> mys;
    for(int i=1; ; ++i){
        int v=n*i;
        while(v){
            mys.insert(v%10);
            v/=10;
        }
        if(sz(mys)==10) return n*i;
    }
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1; i<=T; ++i){
        int v;
        scanf("%d",&v);
        v=go(v);
        printf("Case #%d: ",i);
        if(v==-1) puts("INSOMNIA");
        else printf("%d\n",v);
    }
}

