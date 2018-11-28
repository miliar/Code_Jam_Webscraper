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

char st[1009];

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int cas; scanf("%d",&cas);
    rep(cs,cas) {
        scanf("%s",&st);
        string S;
        int n=strlen(st);
        S=st[0];
        rep(i,n-1) {
            if (st[i]+S < S+st[i]) S=S+st[i];
                else S=st[i]+S;
        }
        cout<<"Case #"<<cs<<": ";
        cout<<S<<endl;
    }
    return 0;
}
