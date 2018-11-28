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
typedef complex<ll> pt;

int T, pals[10000001];
ll A, B;

bool isPal(ll num)
{
    int store[15], dig = 0;
    while (num) store[dig++] = num%10, num/=10;
    for (int i = 0; 2*i < dig; ++i)
        if (store[i] != store[dig-1-i])
            return false;
    return true;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    pals[0] = 0;
    for (int i = 1; i <= 10000000; ++i)
        pals[i] = pals[i-1] + (isPal(i) && isPal(i*i));
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> A >> B;
        int ans = pals[(int)sqrt(B+0.5)] - pals[(int)sqrt(A-0.5)];
        cout << "Case #" << z << ": " << ans << endl;
    }
}
