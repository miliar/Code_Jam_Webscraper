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

map<pair<int,int> , int> _dp;

int N, P, Q;

const int MAXN = 1024;

int h[MAXN], g[MAXN];

int dp(int i, int k)
{
    if (i >= N) return 0;
    const pair<int,int> par = make_pair(i,k);
    map<pair<int,int> , int>::iterator it = _dp.find(par);
    if (it != _dp.end())
        return it->second;
    // Calculo posta
    int towerShots = ((h[i] + Q - 1) / Q);
    int ret = dp(i+1, k + towerShots ); // No lo mato
    int remanent = h[i]; while (remanent > Q) remanent -= Q;
    int neededShots = (remanent + P - 1) / P;
    if (neededShots <= towerShots + k)
        ret = max(ret, g[i] + dp(i+1, k + towerShots - 1 - neededShots)); // Puede ser -1 el k pero creo que no se caga, significa que la torre dispara una vez antes que nos.
    _dp[par] = ret;
    return ret;
}

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        _dp.clear();
        cin >> P >> Q >> N;
        forn(i,N) cin >> h[i] >> g[i];
        printf("Case #%d: %d\n" , tt+1, dp(0,0));
    }
    return 0;
}
