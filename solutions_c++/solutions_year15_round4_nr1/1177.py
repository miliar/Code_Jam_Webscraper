
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)
#define MIN(x,y) ( ((x) < (y))? (x) : (y) )
#define MAX(x,y) ( ((x) > (y))? (x) : (y) )
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define INF 1000000001

using namespace std;

typedef pair < int , int > PII;
typedef long long int LLI;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;

void solve()
{
    int r, c;
    cin >> r >> c;

    char T[r][c];

    FOR(i,0,r-1) FOR(j,0,c-1)
        cin >> T[i][j];

    int ans = 0;

    FOR(i,0,r-1) FOR(j,0,c-1)
        if (T[i][j] != '.')
        {
            bool firstInRow = 1,
                 lastInRow = 1,
                 firstInCol = 1,
                 lastInCol = 1;

            FOR(k,0,j-1)
                if (T[i][k] != '.')
                    firstInRow = 0;

            FOR(k,j+1,c-1)
                if (T[i][k] != '.')
                    lastInRow = 0;

            FOR(k,0,i-1)
                if (T[k][j] != '.')
                    firstInCol = 0;

            FOR(k,i+1,r-1)
                if (T[k][j] != '.')
                    lastInCol = 0;

            int sum = firstInRow + lastInRow +
                      firstInCol + lastInCol;

            if (sum == 4)
            {
                cout << "IMPOSSIBLE";
                return ;
            }

            bool toBeChanged = 0;

            bool b[] = {firstInRow, lastInRow, firstInCol, lastInCol};
            char c[] = {'<', '>', '^', 'v'};

            FOR(k,0,3)
                if (b[k] && (T[i][j] == c[k]))
                    toBeChanged = 1;

            ans += toBeChanged;
        }

    cout << ans;
}

/*************************************************************************/

int main()
{
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    FOR(i,1,t)
    {
        cout << "Case #" << i << ": ";
        solve();

        cout << '\n';
    }

    return 0;
}

/*************************************************************************/
