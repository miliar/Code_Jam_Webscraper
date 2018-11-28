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
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;
typedef complex<ll> pt;

int T, P;
ll E[10000], F[10000];
vector<ll> absval, remsum;

bool solve(int pos, ll sum)
{
    if (sum == E[0])
        return true;
    if (E[0] > sum || E[0] < sum - remsum[pos])
        return false;
    absval[pos] *= -1;
    if (solve(pos+1, sum + absval[pos]))
        return true;
    absval[pos] *= -1;

    int j = pos+1;
    while (j < P && absval[pos] == absval[j])
        ++j;
    return solve(j, sum);
}

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        absval.clear();
        cin >> P;
        for (int i = 0; i < P; ++i)
            cin >> E[i];
        for (int i = 0; i < P; ++i)
            cin >> F[i];

        while (F[0] >= 2)
        {
            absval.push_back(0);
            for (int i = 0; i < P; ++i)
                F[i] /= 2;
        }
        for (int i = 1; i < P; ++i)
        if (F[i])
        {
            absval.push_back(E[i]-E[0]);
            int j = 0, k = i;
            while (j < P && k < P)
            {
                if (!F[j])
                    ++j;
                else if (E[k]-E[j] == absval.back())
                    F[k] -= F[j], ++j, ++k;
                else
                    ++k;
            }
            --i;
        }
        sort(absval.begin(), absval.end());
        reverse(absval.begin(), absval.end());
        remsum.resize(absval.size()+1);
        remsum.back() = 0;
        for (int i = absval.size()-1; i >= 0; --i)
            remsum[i] = remsum[i+1] + absval[i];
        solve(0, 0);
        sort(absval.begin(), absval.end());
        cout << "Case #" << z << ":";
        for (int i = 0; i < absval.size(); ++i)
            cout << ' ' << absval[i];
        cout << endl;
    }
}
