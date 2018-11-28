#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>
#include <deque>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        string s; cin >> s;
        deque<char> op;
        for (const auto &c : s)
        {
            if (op.size() == 0)
                op.push_front(c);
            else if (c >= op.front())
                op.push_front(c);
            else
                op.push_back(c);
        }

        cout << "Case #" << t << ": ";
        for (const auto &it : op)
        {
            cout << it;
        }
        cout << endl;
    }

    return 0;
}
