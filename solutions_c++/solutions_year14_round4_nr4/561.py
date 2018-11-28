//Krzysztof Pieprzak
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<long long, long long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

#define Size(x) (int)x.size()
#define VAR(v,n) typeof(n)v = (n)
#define FOR(i,a,b) for(VAR(i,a); i < (b); ++i)
#define FORE(i,a,b) for(VAR(i,a); i <= (b); ++i)
#define FORREV(i,a,b) for(VAR(i,b); i >= (a); --i)
#define FORSTEP(i,a,b,step) for(VAR(i,a); i < (b); i += (step))
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define ALL(x) x.begin(),x.end()
#define CLEAR(t) memset(t, 0, sizeof(t))
#define F first
#define S second
#define MP make_pair
#define PUB push_back
#define POB pop_back
#define pieprzu ios_base::sync_with_stdio(0);

const int    INF = 1000000001;
const double EPS = 10e-9;

const int MAXM = 10;
const int MAXN = 5;
const int SIZE = 15;

char s[MAXM][SIZE];
int nn[MAXM];
int id[MAXM];

int tab[MAXN][MAXM];
int len[MAXN];

int n,m;

int MX;
int CNT;

bool cmp(const int &a, const int &b)
{
    for (int i=0,j=0; i<nn[a] && j<nn[b]; ++i,++j)
        if (s[a][i] != s[b][j])
            return s[a][i] < s[b][j];
    return nn[a]<nn[b];
}

inline void fun()
{
    int cnt = 0;
    FOR (i, 0, n)
    {
        if (len[i]) cnt += 1;
        if (len[i]) cnt += nn[tab[i][0]];
        FOR (j, 1, len[i])
        {
            FOR (k, 0, nn[tab[i][j]])
            {
                if (k >= nn[tab[i][j-1]] || s[tab[i][j]][k] != s[tab[i][j-1]][k])
                {
                    cnt += nn[tab[i][j]]-k;
                    break;
                }
            }
        }
    }
    if (MX == cnt) ++CNT;
    else if (MX < cnt)
    {
        MX = cnt;
        CNT = 1;
    }
}

void countSol(int v)
{
    if (v == m)
    {
        fun();
        return;
    }

    int vv = id[v];
    FOR (i, 0, n)
    {
        tab[i][len[i]++] = vv;
        countSol(v+1);
        --len[i];
    }
}

void rob(int tc)
{
    printf("Case #%d: ", tc);

    scanf("%d %d", &m, &n);

    FOR (i, 0, m)
    {
        scanf("%s", s[i]);
        nn[i] = strlen(s[i]);
        id[i] = i;
    }
    sort(id,id+m,cmp);

    MX = -1;
    CNT = -1;
    countSol(0);

    printf("%d %d\n", MX, CNT);
}

int main()
{
    int test = 1;
    scanf("%d", &test);

    FORE (i, 1, test) rob(i);

    return 0;
}
