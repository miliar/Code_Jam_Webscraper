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
	int i, j, n;
	int caseno, t, vella;
	FILE *in, *out;
    in = fopen ("B-large.in", "r");
    out = fopen ("A-small-practice.out", "w");
	fscanf (in, "%d", &t);
	for (caseno = 1; caseno <= t; caseno ++)
	{
        fprintf (out, "Case #%d: ", caseno);
        double c,f,x, ans;
        fscanf (in, "%lf %lf %lf", &c, &f, &x);
        for (n = 0; ; n ++)
        {
            double check = (c / (2 + n * f + f)) + (x / (2 + n * f + f)) - (x / (2 + n * f));
            if (check > 0)
                break;
        }
        ans = 0;
        if (n != 0)
            n -= 1;
        fori (0, n - 1)
            ans += (c / (2 + i * f));

        ans += (x / (2 + n * f));
        fprintf (out, "%.7lf\n", ans);
	}
	return 0;
}
