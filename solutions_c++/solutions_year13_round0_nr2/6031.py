#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

//#define DEBUG  //comment this line to pull out print statements
#ifdef DEBUG
#define TAB '\t'
#define debug(a, end) cout << #a << ": " << a << end
#define dbg(end) end
#else
#define debug(a, end)
#define dbg(end)
#endif

typedef pair<int, int> point;
typedef vector<int> vi; //?
typedef vector<point> vp; //?

#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())   
#define SORT(c) sort((c).begin(),(c).end())   
#define FOR(i,a,b) for (int  i=(a); i < (b); i++)    
#define REP(i,n) FOR(i,0,n)    
#define CL(a,b) memset(a,b,sizeof(a))
#define CL2d(a,b,x,y) memset(a, b, sizeof(a[0][0])*x*y)

/*global variables*/
int lawn[100][100];
int boundx;
int boundy;
int tallest;
/*global variables*/

void dump()
{
    //dump data
}

bool getInput()
{
    //get input
    int h;
    scanf("%d %d ", &boundx, &boundy);

    REP(i, boundx)
    {
        REP(j, boundy)
        {
            scanf("%d ", &h);
            lawn[i][j] = h;
            tallest = max(tallest, h);
        }
    }
    
    return true;
}

bool check_pos(int x, int y, int n)
{
    bool can_up = true;
    bool can_right = true;
    bool can_left = true;
    bool can_down = true;

    //go right
    FOR(i, y, boundy)
    {
        if (lawn[x][i] != n)
        {
            debug(i, TAB); debug(x, TAB); debug(n, TAB); debug(lawn[x][i], endl);
            can_right = false;
        }
    }

    //go left
    FOR(i, 0, y)
    {
        if (lawn[x][i] != n)
        {
            debug(i, TAB); debug(x, TAB); debug(n, TAB); debug(lawn[x][i], endl);
            can_left = false;
        }
    }

    //go down
    FOR(i, x, boundx)
    {
        if (lawn[i][y] != n)
        {
            debug(i, TAB); debug(y, TAB); debug(n, TAB); debug(lawn[i][y], endl);
            can_down = false;
        }
    }

    //go up
    FOR(i, 0, x)
    {
        if (lawn[i][y] != n)
        {
            debug(i, TAB); debug(y, TAB); debug(n, TAB); debug(lawn[i][y], endl);
            can_up = false;
        }
    }

    return (can_down && can_up) || (can_left && can_right);
}

void process()
{
    //process input
    debug(tallest, endl);
    bool can_do = true;
    REP(i, boundx)
    {
        REP(j, boundy)
        {
            if (lawn[i][j] != tallest)
                can_do = check_pos(i, j, lawn[i][j]);
            if (!can_do) break;
        }
        if (!can_do) break;
    }


    printf("%s\n", can_do ? "YES" : "NO");
}

int main()
{
    int nc = 0;
    int count = 0;
    scanf("%d ", &nc);
    while (nc-- > 0)
    {
        printf("Case #%d: ", ++count);
        getInput();
        process();

        /*CLEAR GLOBAL VARIABLES!*/
        tallest = 0;
        /*CLEAR GLOBAL VARIABLES!*/
    }

    return 0;
}
