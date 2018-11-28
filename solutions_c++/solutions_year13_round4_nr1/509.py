#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define FOR(a,b,c) for (int a=b,_c=c;a<=_c;a++)
#define FORD(a,b,c) for (int a=b;a>=c;a--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define REPD(i,a) for(int i=(a)-1; i>=0; --i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn=2007;

struct edge{
    int x,y,p;
}a[maxn];

int n,m,T;
ll res,sum;

bool cmp(const edge &a, const edge &b){
    return a.x<b.x || (a.x==b.x && a.y<b.y);
}

multiset<pii> mys;

ll cal(ll len){
    return len*(len-1)/2;
}

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    FOR(tt,1,T){
        scanf("%d%d",&n,&m);
        int l,r,p;
        res=sum=0;
        FOR(i,1,m){
            scanf("%d%d%d",&l,&r,&p);
            a[i].x=l; a[i].y=0; a[i].p=p;
            a[i+m].x=r; a[i+m].y=1; a[i+m].p=p;
            sum+=cal(r-l)*p;
        }
        sort(a+1,a+m*2+1,cmp);
        mys.clear();
        pii node;
        FOR(i,1,m*2)
            if(a[i].y==0){
                mys.insert(pii(-a[i].x,a[i].p));
            }else{
                while(a[i].p>0){
                    node=*mys.begin();
                    mys.erase(mys.begin());
                    int v=min(node.se, a[i].p);
                    res+=cal(a[i].x + node.fi)*v;
                    node.se -= v;
                    a[i].p -= v;
                    if(node.se > 0) mys.insert(node);
                }
            }
        printf("Case #%d: %lld\n",tt,res-sum);
    }

    return 0;
}
