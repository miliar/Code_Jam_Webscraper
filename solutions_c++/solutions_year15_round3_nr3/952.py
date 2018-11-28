#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)

using namespace std;

int test(vector<int> &DP)
{
    int N = sz(DP);

    FOR(i,0,N)
    if(!DP[i]) return i;

    return 0;
}
int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {
        int C,D,V; cin>>C>>D>>V;
        vector<int> DP(V+1,0), A;

        int a;
        FOR(d,0,D) { cin>>a; A.push_back(a); }

        DP[0] = 1;

        int coin;

        FOR(d,0,D)
        {
            coin = A[d];

            for(int j = V; j >= coin; --j)
            {
                DP[j] |= DP[j-coin];
            }
        }

        int ans = 0;
        while(coin = test(DP))
        {
            ++ans;

            for(int j = V; j >= coin; --j)
            {
                DP[j] |= DP[j-coin];
            }
        }

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }

    return 0;
}
// END KAWIGIEDIT TESTING

//Powered by KawigiEdit 2.1.4 (beta) modified by pivanof!
