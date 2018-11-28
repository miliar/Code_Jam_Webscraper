
#include <iostream>
#include <vector>
#include <algorithm>

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

    FOR(i,1,t)
    {
        int n;
        cin >> n;

        vector < double > N(n);
        vector < double > K(n);

        FOREACH(j,N) cin >> N[j];
        FOREACH(j,K) cin >> K[j];

        sort(N.begin(), N.end());
        sort(K.begin(), K.end());

        int it = 0, score = 0;

        FOREACH(j,N) if (N[j] > K[it])
        {
            ++score;
            ++it;
        }
        cout << "Case #" << i << ": ";
        cout << score;

        score = 0;
        FOREACH(j,N)
        {
            if (K[SIZE(K)-1] < N[j])
                ++score;
            else
            {
                vector < double >::iterator k = K.begin();

                while ((*k) < N[j]) ++k;

                K.erase(k);
            }
        }

        cout << " " << score << endl;
    }



    return 0;
}

/************************************************************/
