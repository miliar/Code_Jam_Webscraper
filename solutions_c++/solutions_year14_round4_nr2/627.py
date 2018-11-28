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

const int MAXN = 1005;

int t[MAXN];
int tS[MAXN];

inline void shift1(int a, int b)
{
    FORREV (i, a+1, b) t[i] = t[i-1];
}

inline void shift2(int a, int b)
{
    FOR (i, a, b) t[i] = t[i+1];
}

void rob(int tc)
{
    printf("Case #%d: ", tc);

    int n;
    scanf("%d", &n);

    FOR (i, 0, n)
    {
        scanf("%d", &t[i]);
        tS[i] = t[i];
    }
    sort(tS,tS+n);

    int bg = 0;
    int ed = n-1;
    int cnt = 0;
    int pos = -1;
    FOR (i, 0, n)
    {
        pos = -1;
        FORE (j, bg, ed)
            if (t[j] == tS[i])
            {
                pos = j;
                break;
            }

        assert(pos != -1);

        if (pos-bg < ed-pos)
        {
            cnt += pos-bg;
            shift1(bg,pos);
            ++bg;
        }
        else
        {
            cnt += ed-pos;
            shift2(pos,ed);
            --ed;
        }
    }

    printf("%d\n", cnt);
}

int main()
{
    int test = 1;
    scanf("%d", &test);

    FORE (i, 1, test) rob(i);

    return 0;
}
