#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

typedef long long tint;

const int MAXN = 1024;

int v[MAXN], position[MAXN];

int lc[MAXN][MAXN];
int rc[MAXN][MAXN];
int dp[MAXN];

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        int N; cin >> N;
        map<int,int> pos;
        forn(i,N){ cin >> v[i]; pos[v[i]] = i;}
        int num = 0;
        forall(it, pos)
        {
            position[num] = it->second;
            v[it->second] = num++;
        }
        forn(i,N+1)
            lc[i][0] = 0;
        forn(i,N+1)
        forsn(j,1,N)
            lc[i][j] = lc[i][j-1] + (v[j-1] >= i);
            
        forn(i,N+1)
            rc[i][N-1] = 0;
        forn(i,N+1)
        dforn(j,N-1)
            rc[i][j] = rc[i][j+1] + (v[j+1] >= i);
        
        
        // Caso base: i == N, puse todo
        dp[N] = 0;
        dforn(i, N)
        {
            dp[i] = min(dp[i+1] + lc[i][position[i]], dp[i+1] + rc[i][position[i]]);
        }
        printf("Case #%d: %d\n" , tt+1, dp[0]);
    }
    return 0;
}

