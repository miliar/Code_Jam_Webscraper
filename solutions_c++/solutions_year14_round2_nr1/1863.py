
#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>

using namespace std;

#define FOR(i,b,e) for(int i=(b); i<=(e); ++i)
#define FORD(i,b,e) for(int i=(b); i>=(e); --i)
#define SIZE(c) (int) c.size()
#define FOREACH(i,c) FOR(i,0,SIZE(c)-1)
#define PB push_back

#define MIN(a,b) ( ((a)<=(b))? (a) : (b) )
#define MAX(a,b) ( ((a)>=(b))? (a) : (b) )

inline int abs(int x)
{
    if (x >= 0) return x;
    return (-x);
}

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
        int n, res = 0;
        cin >> n;

        vector < string > S(n);
        FOREACH(i,S) cin >> S[i];

        vector < string > base(n);
        vector < vector < int > > C(n);

        FOREACH(i,S)
        {
            base[i] = S[i][0];
            FOR(j,1,SIZE(S[i])-1) if(S[i][j] != S[i][j-1])
                base[i] += S[i][j];
        }

        vector < int > sum(SIZE(base[0]),0);

        FOR(i,1,SIZE(S)-1) if(base[i] != base[i-1])
        {
            ans.PB(-1);
            goto nextcase;
        }

        FOREACH(i,C) C[i].resize(SIZE(base[i]),0);

        FOREACH(i,S)
        {
            int it = 0;
            FOREACH(j,S[i])
            {
                if (S[i][j] == base[i][it])
                    ++C[i][it];
                else
                    ++C[i][++it];
            }
        }

        FOREACH(i,C) FOREACH(j,C[i])
            sum[j] += C[i][j];

        FOREACH(i,sum)
            sum[i] = ( sum[i] + (int) (n/2) ) / n;

        FOREACH(i,C) FOREACH(j,C[i])
            res += abs( sum[j] - C[i][j] );

        ans.PB(res);

        nextcase:;
    }

    FOREACH(i,ans)
    {
        cout << "Case #" << (i+1) << ": ";

        if (ans[i] < 0) cout << "Fegla Won" << '\n';
        else cout << ans[i] << '\n';
    }


    return 0;
}

/************************************************************/
