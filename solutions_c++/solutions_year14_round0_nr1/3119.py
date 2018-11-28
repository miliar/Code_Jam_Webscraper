
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i,b,e) for(int i=(b); i<=(e); ++i)
#define FORD(i,b,e) for(int i=(b); i>=(e); --i)
#define SIZE(c) (int) c.size()
#define FOREACH(i,c) FOR(i,0,SIZE(c)-1)
#define PB push_back

/************************************************************/

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    FOR(i,1,t)
    {
        vector < bool > V(16,1);

        int x;
        cin >> x;

        FOR(r,1,4) FOR(k,1,4)
        {
            int y;
            cin >> y;

            if (r != x) V[y-1] = 0;
        }

        cin >> x;

        FOR(r,1,4) FOR(k,1,4)
        {
            int y;
            cin >> y;

            if (r != x) V[y-1] = 0;
        }

        int one = -1, sum = 0;
        cout << "Case #" << i << ": ";

        FOREACH(j,V) if (V[j])
        {
            ++sum;

            if (one == -1) one = j+1;
            else if (sum == 2)
                cout << "Bad magician!";
        }

        if (one == -1)
            cout << "Volunteer cheated!";
        else if (sum == 1)
            cout << one;

        cout << endl;
    }



    return 0;
}

/************************************************************/
