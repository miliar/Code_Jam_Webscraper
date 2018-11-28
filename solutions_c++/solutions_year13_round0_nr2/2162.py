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
/*#include <hash_map>
using namespace __gnu_cxx;*/

typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;
const int MX = 109;
int pat[MX][MX];
int di[]={0, 0, 1, -1};
int dj[]={1, -1, 0, 0};
int n, m;

bool isLessOrEq(int i, int j, int d, int nm) {
	int ni = i, nj = j;
	while(ni>=0 && nj>=0 && ni < n && nj < m) {
		if(pat[ni][nj]>nm)
			return false;
		ni+=di[d];
		nj+=dj[d];
	}
	return true;
}
bool canpass(int i, int j) {
	if((isLessOrEq(i, j, 0, pat[i][j]) && isLessOrEq(i, j, 1, pat[i][j])) || (isLessOrEq(i, j, 2, pat[i][j]) && isLessOrEq(i, j, 3, pat[i][j])))
		return true;
	return false;
}
int main() {

	//	std::ios_base::sync_with_stdio(false);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.txt", "wt", stdout);

	int t;scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		cout<<"Case #"<<ii+1<<": ";

		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", pat[i]+j);
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if(!canpass(i, j)) {
					cout<<"NO\n";
					goto bara;
				}
			}
		}
		cout<<"YES\n";
		bara:;
	}
	
	return 0;
}
