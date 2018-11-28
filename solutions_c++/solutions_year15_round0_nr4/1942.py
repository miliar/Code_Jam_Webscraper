#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cassert>
#include<climits>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
#define INF (1ll<<62)
using namespace std;
int main ()
{
    int a[5][5][5]= {};
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++)
        {
            a[1][i][j] = 1;
            if ((i * j) % 2 == 0) a[2][i][j] = 1;
        }
    a[3][2][3] = a[3][3][2] = a[3][3][3] = a[3][4][3] = a[3][3][4] = 1;
    a[4][3][4] = a[4][4][3] = a[4][4][4] = 1;
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: %s\n", ++cas, a[x][r][c] == 1 ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
