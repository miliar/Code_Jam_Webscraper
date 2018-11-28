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
    LL T; cin >> T;
    for (LL t = 1; t <= T; ++t)
    {
        LL N; cin >> N;
        if (N == 0)
        {
            cout << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }

        LL curr_num = 0;
        set<LL> di;
        while (di.size() < 10)
        {
            curr_num += N;
            LL tmp = curr_num;
            while (tmp > 0)
            {
                di.insert(tmp % 10);
                tmp /= 10;
            }
        }

        cout << "Case #" << t << ": " << curr_num << endl;
    }

    return 0;
}
