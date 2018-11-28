#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <queue>
#include <cmath>

using namespace std;

static const string _q = "B";

struct sol
{
    vector<double> probs;
    int n_assigned;
    int last_assigned;
};

void solve()
{
    int N, K; cin >> N >> K;

    vector<double> p(N);

    for (int i = 0; i < N; i++)
    { 
        cin >> p[i];
    }

    sol s;
    s.probs.resize(K/2 + 1, 0);
    s.probs[0] = 1;    
    s.n_assigned = 0;
    s.last_assigned = -1;

    queue<sol> q;
    q.push(s);

    double max_prob = 0;

    while(!q.empty())
    {
        s = q.front(); q.pop();
        
       
        if (s.n_assigned == K)
        {
            if (s.probs[K/2] > max_prob)
                max_prob = s.probs[K/2];

            continue;
        }

        for (int i = s.last_assigned+1; i < N-K+1+s.n_assigned; i++)
        {
            sol s1 = s;
            s1.probs[0] = s.probs[0] * (1 - p[i]);
            for (int j = 1; j <= K/2; j++)
            {
                s1.probs[j] = s.probs[j-1] * p[i] + s.probs[j] * (1 - p[i]);
            }
            s1.n_assigned++;
            s1.last_assigned = i;
            q.push(s1);
        }
    }

    cout << max_prob;
}

int main(void)
{
    ifstream in(_q + ".in");
    ofstream out(_q + ".out");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());

    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
