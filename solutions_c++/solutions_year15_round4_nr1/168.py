#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

const int MAXN = 256;

string v[MAXN];
char cuenta[MAXN][MAXN];
char visto[MAXN][MAXN];

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        memset(cuenta,0,sizeof(cuenta));
        memset(visto,0,sizeof(cuenta));
        int R,C; cin >> R >> C;
        forn(i,R) cin >> v[i];
        forn(i,R)
        {
            int j;
            for(j = 0; j < C && v[i][j] == '.' ;j++);
            if (j < C && v[i][j] == '<') cuenta[i][j]++;
            if (j < C) visto[i][j]++;
            for(j = C-1; j >= 0 && v[i][j] == '.' ;j--);
            if (j >= 0 && v[i][j] == '>') cuenta[i][j]++;
            if (j >= 0) visto[i][j]++;
        }
        forn(j,C)
        {
            int i;
            for(i = 0; i < R && v[i][j] == '.' ;i++);
            if (i < R && v[i][j] == '^') cuenta[i][j]++;
            if (i < R) visto[i][j]++;
            for(i = R-1; i >= 0 && v[i][j] == '.' ;i--);
            if (i >= 0 && v[i][j] == 'v') cuenta[i][j]++;
            if (i >= 0) visto[i][j]++;
        }
        int res = 0;
        bool noSePuede = false;
        forn(i,R)
        forn(j,C)
        {
            res += (cuenta[i][j] > 0);
            if (visto[i][j] == 4) noSePuede = true;
        }
        if (noSePuede)
            cout << "Case #" << caso + 1 << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
