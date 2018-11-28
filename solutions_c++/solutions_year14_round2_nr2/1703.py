
#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <queue>

using namespace std;

#define FOR(i,b,e) for(int i=(b); i<=(e); ++i)
#define FORD(i,b,e) for(int i=(b); i>=(e); --i)
#define SIZE(c) (int) c.size()
#define FOREACH(i,c) FOR(i,0,SIZE(c)-1)
#define PB push_back

#define MIN(a,b) ( ((a)<=(b))? (a) : (b) )
#define MAX(a,b) ( ((a)>=(b))? (a) : (b) )

typedef long long int lli;

/************************************************************/

int main()
{
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    vector < int > ans;

    FOR(i,1,t)
    {
        int a, b, k;
        cin >> a >> b >> k;

        int res = 0;

        FOR(p,0,a-1) FOR(q,0,b-1) if ((p&q) < k)
            ++res;

        ans.PB(res);
    }

    FOREACH(i,ans)
    {
        cout << "Case #" << (i+1) << ": ";
        cout << ans[i] << '\n';
    }

    return 0;
}

/************************************************************/
