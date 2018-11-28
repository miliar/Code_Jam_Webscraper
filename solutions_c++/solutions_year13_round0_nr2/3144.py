/*
 *Author:       Zhaofa Fang
 *Created time: 2013-04-13-10.50
 *Language:     C++
 */
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,s,t) for(int i = (s);i <= (t);i++)
#define FORD(i,s,t) for(int i = (s);i >= (t);i--)
#define REP(i,n) FOR(i,0,n-1)
#define REPD(i,n) FORD(i,n-1,0)
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
#define ft first
#define sd second
#define lowbit(x) (x&(-x))
#define INF (1<<30)


int maz[110][110],a[110][110];

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	FOR(cas,1,T){
        int n,m;
        scanf("%d%d",&n,&m);
        REP(i,n)REP(j,m)scanf("%d",&maz[i][j]);
        REP(i,n){
            int mx = 0;
            REP(j,m)mx = max(mx,maz[i][j]);
            REP(j,m)a[i][j] = mx;
        }
        REP(j,m){
            bool flag = 0;
            int mi = 110;
            REP(i,n)if(maz[i][j]!=a[i][j])flag = 1;
            if(flag){
                REP(i,n){
                    if(a[i][j]==maz[i][j])continue;
                    mi = min(mi,maz[i][j]);
                }
                REP(i,n)if(a[i][j]>mi)a[i][j] = mi;
            }
        }
        bool OK = 1;
        REP(i,n){
            REP(j,m)if(a[i][j] != maz[i][j])OK = 0;
        }
        printf("Case #%d: ",cas);
        if(OK)puts("YES");
        else puts("NO");
	}
	return 0;
}
