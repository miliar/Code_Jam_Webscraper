#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int N, M;
int a[128][128];

int main(void)	{
	int T;
	
	cin >> T;
	FOR (nc, 1, T+1) {
		cin >> N >> M;
		FOR (i, 0, N)	FOR (j, 0, M)	cin >> a[i][j];
		
		bool possible = true;
		FOR (i, 0, N)	{
			if (!possible)	break;
			FOR (j, 0, M)	{
				bool can = true;
				FOR (k, 0, M)	if (a[i][k] > a[i][j])	can = false;
				if (can)	continue;
				can = true;
				FOR (k, 0, N)	if (a[k][j] > a[i][j])	can = false;
				if (!can)	{
					possible = false;
					break;
				}
			}
		}
		
		cout << "Case #" << nc << ": " << (possible ? "YES" : "NO") << endl;
	}
}
