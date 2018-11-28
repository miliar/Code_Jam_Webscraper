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
typedef complex<ll> pt;

int T, N, X, S[10000];

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
    	cin >> N >> X;
    	for (int i = 0; i < N; ++i)
    		cin >> S[i];
    	sort(S, S+N);
    	int ans = 0;
    	int i = 0, j = N-1;
    	while (i < j)
    	{
    		if (S[i] + S[j] <= X)
    			++i;
    		--j;
    		++ans;
    	}
    	if (i == j)
    		++ans;
    	cout << "Case #" << z << ": " << ans << endl;
    }
}
