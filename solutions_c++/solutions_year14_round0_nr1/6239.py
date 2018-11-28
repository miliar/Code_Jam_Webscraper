/*
    Solved By : Kazi Mahbubur Rahman (MAHBUB)
                Software Engineer,
                Samsung R&D Institute Bangladesh (SRBD),
                Dhaka, Bangladesh.
    Time :
    Rank :
    Complexity:
*/

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define FOR(i, L, U) for(int i=(int)L; i<=(int)U; i++)
#define FORD(i, U, L) for(int i=(int)U; i>=(int)L; i--)

#define READ(x) freopen(x, "r", stdin)
#define WRITE(x) freopen(x, "w", stdout)

#define PQ priority_queue
#define PB push_back
#define SZ size()

#define EPS 1e-9
#define SQR(x) ((x)*(x))
#define INF 99999999
#define TO_DEG 57.29577951
#define PI 2*acos(0.0)

typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector< vector<bool> > VVB;
typedef pair<int, int> PII;
typedef map<int, int> MII;
typedef map<char, int> MCI;
typedef map<string, int> MSI;

int GCD(int a,int b){   while(b)b^=a^=b^=a%=b;  return a;   }

// UP, RIGHT, DOWN, LEFT, UPPER-RIGHT, LOWER-RIGHT, LOWER-LEFT, UPPER-LEFT
int dx[8] = {-1, 0, 1, 0, -1, 1,  1, -1};
int dy[8] = { 0, 1, 0,-1,  1, 1, -1, -1};

// Represents all moves of a knight in a chessboard
int dxKnightMove[8] = {-1, -2, -2, -1,  1,  2, 2, 1};
int dyKnightMove[8] = { 2,  1, -1, -2, -2, -1, 1, 2};

inline int src() { int ret; scanf("%d", &ret); return ret; }

#define WHITE 0
#define GRAY 1
#define BLACK 2

#define MAX_NODE 10001

int grid1[4][4];
int grid2[4][4];
int ans1, ans2;
set<int> candidates;

int main()
{
    READ("A-small-attempt2.in");
    WRITE("output.txt");
    int i, j, k;
    int TC, tc;

    TC = src();

    FOR(tc, 1, TC) {
        ans1 = src();
        FOR(i, 0, 3) FOR(j, 0, 3) scanf("%d", &grid1[i][j]);
        ans2 = src();
        FOR(i, 0, 3) FOR(j, 0, 3) scanf("%d", &grid2[i][j]);

        FOR(i, 0, 3) candidates.insert(grid1[ans1-1][i]);
        FOR(i, 0, 3) candidates.insert(grid2[ans2-1][i]);

        if(candidates.size() <= 6) {
            printf("Case #%d: Bad magician!\n", tc);
            candidates.clear();
            continue;
        }
        if(candidates.size() == 8) {
            printf("Case #%d: Volunteer cheated!\n", tc);
            candidates.clear();
            continue;
        }
        FOR(i, 0, 3) {
            int temp = grid1[ans1-1][i];
            bool isFound = false;
            FOR(j, 0, 3) {
                if(temp == grid2[ans2-1][j]) {
                    isFound = true;
                    break;
                }
            }
            if(isFound) {
                printf("Case #%d: %d\n", tc, temp);
                break;
            }
        }
        candidates.clear();


    }

    return 0;
}


