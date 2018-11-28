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

int T, N;
ld nao[1000], ken[1000];

int solve()
{
	int score = 0, i = 0, j = 0;
	while (i < N && j < N)
	{
		if (nao[i] > ken[j])
			++score, ++i, ++j;
		else
			++i;
	}
	return score;
}

int main()
{
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(9);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
    	cin >> N;
    	for (int i = 0; i < N; ++i)
    		cin >> nao[i];
    	for (int i = 0; i < N; ++i)
    		cin >> ken[i];
    	sort(nao, nao+N);
    	sort(ken, ken+N);
    	cout << "Case #" << z << ": ";
    	cout << solve() << ' ';
    	for (int i = 0; i < N; ++i)
    		swap(nao[i], ken[i]);
    	cout << (N-solve()) << endl;
    }
}
