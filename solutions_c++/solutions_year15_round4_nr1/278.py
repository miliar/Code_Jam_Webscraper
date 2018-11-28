#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

const int MAX = 110;
const int inf = 1<<22;
int R, C;
char grid[MAX][MAX];
bool grid_right[MAX][MAX];
bool grid_left[MAX][MAX];
bool grid_down[MAX][MAX];
bool grid_up[MAX][MAX];


int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(cnt,0,T){
		cin >> R >> C;
		FOR(i,0,R) FOR(j,0,C)
			cin >> grid[i][j];

		FOR(i,0,R){
			bool flag = false;
			ROF(j,0,C){
				grid_right[i][j] = flag;
				if(grid[i][j] != '.')
					flag = true;
			}
		}
		FOR(i,0,R){
			bool flag = false;
			FOR(j,0,C){
				grid_left[i][j] = flag;
				if(grid[i][j] != '.')
					flag = true;
			}
		}
		FOR(j,0,C){
			bool flag = false;
			ROF(i,0,R){
				grid_down[i][j] = flag;
				if(grid[i][j] != '.')
					flag = true;
			}
		}
		FOR(j,0,C){
			bool flag = false;
			FOR(i,0,R){
				grid_up[i][j] = flag;
				if(grid[i][j] != '.')
					flag = true;
			}
		}

		int ans = 0;
		FOR(i,0,R) FOR(j,0,C) if(grid[i][j] != '.'){
			if(grid[i][j] == '>' && grid_right[i][j])
				continue;
			if(grid[i][j] == '<' && grid_left[i][j])
				continue;
			if(grid[i][j] == '^' && grid_up[i][j])
				continue;
			if(grid[i][j] == 'v' && grid_down[i][j])
				continue;
			if(grid_right[i][j] || grid_left[i][j] || grid_up[i][j] || grid_down[i][j])
				ans++;
			else
				ans = inf;
		}

		cout << "Case #" << cnt+1 << ": ";
		if(ans < inf)
			cout << ans << '\n';
		else
			cout << "IMPOSSIBLE\n";


	}
	

	return 0;
}
