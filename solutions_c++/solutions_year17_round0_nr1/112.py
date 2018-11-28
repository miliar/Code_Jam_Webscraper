#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;
const long inf = 1000000021L*1000000021L;
int testcase;

void solve()
{
    string S;
    long K;
    cin >> S >> K;
    long len = S.size();

    long flips = 0;
    for(int i = 0; i < len - K + 1; i++)
    {
        if(S[i] == '+')
            continue;
        flips += 1;
        for(int j = i; j < i + K; j++)
            S[j] = (S[j] == '+'? '-' : '+');
    }
    for(int i = len - K + 1; i < len; i++)
        if(S[i] == '-')
        {
            cout << "IMPOSSIBLE";
            return;
        }
    cout << flips;
}

int main()
{
    cout.precision(10);
    int T;
    cin >> T;
    for(testcase = 1; testcase <= T; testcase++)
    {
        cout << "Case #" << testcase << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

