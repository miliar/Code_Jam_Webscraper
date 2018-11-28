#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl;
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x, a) memset(x, (a), sizeof(x))
#define ALL(v) (v).begin(), (v).end()
typedef long long LL;
const double PI = acos(-1.0);
const double eps = 1e-8;
#define INPUT_FILE "in.txt"
#define OUTPUT_FILE "out.txt"

bool is_end = false;
int board[105][105];

bool check_all(int max_row[], int max_col[], int n, int m)
{
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            if (board[i][j] < max_row[i] && board[i][j] < max_col[j])
                return false;
        }
    }
    return true;
}

void proc(int cs)
{
    int n,m;
    int max_row[105] = {};
    int max_col[105] = {};

    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i) 
    {
        for (int j = 0; j < m; ++j)
        {
            scanf("%d", &board[i][j]);
            if (board[i][j] > max_row[i]) max_row[i] = board[i][j];
            if (board[i][j] > max_col[j]) max_col[j] = board[i][j];
        }
    }

    bool ret = check_all(max_row, max_col, n, m);
    printf("Case #%d: ", cs);
    if (ret)
        puts("YES");
    else 
        puts("NO");
}

int main(int argc, char *argv[])
{
    int n;
    freopen(INPUT_FILE, "r", stdin);
    freopen(OUTPUT_FILE, "w", stdout);

    scanf("%d", &n);
    for (int cs = 1; cs <= n; ++cs)
        proc(cs);
   	
	return 0;
}
