/*
 *Author:       Zhaofa Fang
 *Created time: 2014-04-12-10.08 Saturday
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

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,s,t) for(int i = (s);i <= (t);i++)
#define FORD(i,s,t) for(int i = (s);i >= (t);i--)
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n-1);i>=0;i--)
#define PII pair<int,int>
#define PB push_back
#define ft first
#define sd second
#define lowbit(x) (x&(-x))
#define INF (1<<30)
#define eps (1e-8)

const int maxn = 20;
int foo[maxn][maxn],bar[maxn][maxn];
int cnt[maxn];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int T;
    scanf("%d",&T);
    FOR(cas,1,T){
        printf("Case #%d: ",cas);
        int ans1,ans2;
        int n = 4;
        memset(cnt,0,sizeof(cnt));
        scanf("%d",&ans1);
        FOR(i,1,n)FOR(j,1,n)scanf("%d",&foo[i][j]);
        FOR(j,1,n)cnt[foo[ans1][j]]++;
        scanf("%d",&ans2);
        FOR(i,1,n)FOR(j,1,n)scanf("%d",&bar[i][j]);//DEBUG(bar[i][j]);
        FOR(j,1,n)cnt[bar[ans2][j]]++;
        vector<int>tmp;
        FOR(i,1,16)if(cnt[i]==2)tmp.PB(i);
        if(tmp.size()==1)printf("%d\n",tmp[0]);
        else if(tmp.size()==0)puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
    return 0;
}
