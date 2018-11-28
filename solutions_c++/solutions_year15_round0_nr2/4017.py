#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct thing
{
    int num;
    int divisor;

    int turnsRemaining()
    {
        return num / divisor + num % divisor;
    }
};

bool operator < (thing t1, thing t2)
{
    return t1.turnsRemaining() < t2.turnsRemaining();
}

int main (void)
{
    ifstream in("B.in");
    ofstream out("B.op");

    cout.rdbuf(out.rdbuf());

    int T;
    in >> T;

    for (int t = 1; t <= T; t++)
    {
        int D;
    
        in >> D;

        vector<int> P(D);

        for (int i = 0; i < D; i++)
        {
            in >> P[i];
        }

        sort(P.begin(), P.end());

        int maxTurns = P[D-1];

        priority_queue<thing> q;

        for (int i = 0; i < D; i++)
        {
            thing t;
            t.num = P[i];
            t.divisor = 1;
            q.push(t);
        }

        int minTurns = maxTurns;

        int turnCount = 0;

        while(turnCount < maxTurns)
        {
            thing t = q.top();
            q.pop();

            int tr = turnCount + t.turnsRemaining();

            if (tr < minTurns)
            {
                minTurns = tr;
            }

            t.divisor++;
            turnCount++;
            q.push(t);
        }

        cout << "Case #" << t << ": " << minTurns << endl;

    }    

    return 0;
}
