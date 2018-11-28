#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vvi vector< vi >
#define vs vector<string>
#define rep(i,s,e) for(int i=s;i<=e;i++)
#define fori(s,e) for(i=s;i<=e;i++)
#define forj(s,e) for(j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define ull unsigned long long
#define ll signed long long
#define imax INT_MAX
#define imin INT_MIN
#define sz(x) (int)x.size()
#define ppb pop_back
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x));
#define pii pair<int,int>
#define in(c,x) scanf("%"#c,&x);
#define out(c,x) printf("%"#c,x);
#define aa first
#define bb second
#define MOD 1000000007

using namespace std;

int main()
{
	int i, j;
    int caseno, t, vella;
	FILE *in, *out;
    in = fopen ("A-small-attempt0.in", "r");
    out = fopen ("A-small-practice.out", "w");
	fscanf (in, "%d", &t);
    for (caseno = 1; caseno <= t; caseno ++)
    {
        fprintf (out, "Case #%d: ", caseno);
        int ans1, ans2;
        int grid[4][4];
        vector <int> row1, row2;
        fscanf (in, "%d", &ans1);
        fori (0, 3)
            forj (0, 3)
                fscanf (in, "%d", &grid[i][j]);
        forj (0, 3)
            row1.pb (grid[ans1 - 1][j]);
        fscanf (in, "%d", &ans2);
        fori (0, 3)
            forj (0, 3)
                fscanf (in, "%d", &grid[i][j]);
        forj (0, 3)
            row2.pb (grid[ans2 - 1][j]);
        int count = 0;
        int num;
        fori (0, 3)
            forj (0, 3)
                if (row1[i] == row2[j])
                {
                    count ++;
                    num = row1[i];
                }
        if (count == 1)
            fprintf (out, "%d\n", num);
        else if (count == 0)
            fprintf (out, "Volunteer cheated!\n");
        else
            fprintf (out, "Bad magician!\n");
    }
	return 0;
}
