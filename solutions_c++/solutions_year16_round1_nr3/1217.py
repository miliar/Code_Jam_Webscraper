#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define ABS(x) ((x)>0?(x):(-(x)))
#define sqr(x) ((x)*(x))
#define rep(i,n) for (int i=1; i<=(n); i++)
#define For(i,s,t) for (int i=(s); i<=(t); i++)
#define FOR(i,s,t) for (int i=(s); i>=(t); i--)
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)
typedef long long lld;
typedef pair<int,int> pii;

int n,a[20];

int solve() {
    int ans=0,b[20];
    rep(i,n) b[i]=i;
    do {
        if (a[b[1]]==b[2]) {
            For(i,2,n) {
                if (a[b[i]]==b[i-1] || a[b[i]]==b[1]) {
                    bool flag=true;
                    For(j,2,i-1)
                        if (a[b[j]]!=b[j-1] && a[b[j]]!=b[j+1]) flag=false;
                    if (flag) ans=max(ans,i);
                }
            }
        }
        else {
            int i=1;
            while (i<=n && b[i]!=a[b[1]]) i++;
            if (i<=n) {
                bool flag=true;
                if (a[b[i]]!=b[1] && a[b[i]]!=b[i-1]) flag=false;
                For(j,2,i-1)
                    if (a[b[j]]!=b[j-1] && a[b[j]]!=b[j+1]) flag=false;
                if (flag) ans=max(ans,i);
            }
        }
    } while (next_permutation(b+1,b+n+1));
    return ans;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int cas; scanf("%d",&cas);
    rep(cs,cas) {
        scanf("%d",&n);
        rep(i,n) scanf("%d",&a[i]);
        printf("Case #%d: %d\n",cs,solve());
    }
    return 0;
}
