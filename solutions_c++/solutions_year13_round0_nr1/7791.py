#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

#define DEBUG  //comment this line to pull out print statements
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
char board[4][4];
enum DIRECTION { VER, HOR, FS, BS };
/*global variables*/

void dump()
{
    //dump data
}

bool getInput()
{
    //get input
    char line[5];
    
    REP(i, 4)
    {
        scanf("%s ", line);
        REP(j, 4)
        {
            board[i][j] = line[j];
        }
    }
    return true;
}

bool check_pos(int x, int y, char c, DIRECTION d)
{
    switch(d)
    {
    case VER:
        if ((board[x][0] == c || board[x][0] == 'T') &&
            (board[x][1] == c || board[x][1] == 'T') &&
            (board[x][2] == c || board[x][2] == 'T') &&
            (board[x][3] == c || board[x][3] == 'T') ) return true;
        break;
    case HOR:
        if ((board[0][y] == c || board[0][y] == 'T') &&
            (board[1][y] == c || board[1][y] == 'T') &&
            (board[2][y] == c || board[2][y] == 'T') &&
            (board[3][y] == c || board[3][y] == 'T') ) return true;
        break;
    case FS:
        if ((board[0][3] == c || board[0][3] == 'T') &&
            (board[1][2] == c || board[1][2] == 'T') &&
            (board[2][1] == c || board[2][1] == 'T') &&
            (board[3][0] == c || board[3][0] == 'T') ) return true;
        break;
    case BS:
        if ((board[0][0] == c || board[0][0] == 'T') &&
            (board[1][1] == c || board[1][1] == 'T') &&
            (board[2][2] == c || board[2][2] == 'T') &&
            (board[3][3] == c || board[3][3] == 'T') ) return true;
        break;
    }
    return false;
}

void process()
{
    //process input
    bool match = false;
    bool moves_left = false;
    char winner = 0;
    REP(i, 4)
    {
        REP(j, 4)
        {
            if (board[i][j] != '.')
            {
                
                match = check_pos(i, j, board[i][j], VER) ||
                    check_pos(i, j, board[i][j], HOR) ||
                    check_pos(i, j, board[i][j], BS) ||
                    check_pos(i, j, board[i][j], FS);
                if (match) winner = board[i][j];
                match = false;
            }
            else
            {
                moves_left = true;
            }
        }
    }

    if (winner != 0)
        printf("%c won\n", winner);
    else if (moves_left)
        printf("Game has not completed\n");
    else
        printf("Draw\n");
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

        /*CLEAR GLOBAL VARIABLES!*/
    }

    return 0;
}
