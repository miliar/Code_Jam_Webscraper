#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#define REP(i,n) for( int (i)=0;(i)<(int)(n);(i)++)
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
LL LLMAX = 9223372036854775807LL;
const int MOD = 1000000007;
const int maxn = 1000+10;
int m,n;
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};
int G[maxn][maxn];
bool prac;
bool ok(int x,int y){
    return x>=0&&y>=0&&x<m&&y<n;
}

bool downcheck(int i){
    REP(j,m)if(G[j][i]==2)return false;
    return true;
}
bool rightcheck(int i){
    REP(j,n)if(G[i][j]==2)return false;
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;++kase){
        prac = 1;
        scanf("%d %d%*c",&m,&n);
        REP(i,m)REP(j,n)scanf("%d",&G[i][j]);
        REP(i,n)if(G[0][i]!=2)if(downcheck(i))REP(j,m)G[j][i] = 3;
        REP(i,m)if(G[i][0]!=2)if(rightcheck(i))REP(j,n)G[i][j] = 3;
        REP(i,m)REP(j,n)if(G[i][j]==1)prac = 0;
        printf("Case #%d: %s\n",kase,(prac)?"YES":"NO");
    }
}
