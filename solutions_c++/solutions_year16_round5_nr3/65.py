#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int x[1<<10];
int y[1<<10];
int z[1<<10];
int vx[1<<10];
int vy[1<<10];
int vz[1<<10];
int dist[1<<10];
bool visited[1<<10];

int calc_d(int i, int j){
	return (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) + (z[i] - z[j]) * (z[i] - z[j]);
}

struct cmp {
	bool operator()(const int& u, const int& v) {
		if ( dist[u] == dist[v] ) 
			return u < v;
		else return dist[u] < dist[v];
	}
};

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n; cin >> n;
		int s; cin >> s;
		for (int i = 0; i < n; i++)
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		
		for (int i = 0; i < n; i++)
			dist[i] = 0x3f3f3f3f;
		dist[0] = 0;
		
		memset(visited,false,sizeof(visited));
		int cnt = 0;
		while (cnt < n){
			int v = -1;
			int best = 0x3f3f3f3f;
			for (int i = 0; i < n; i++){
				if (!visited[i] && dist[i] < best){
					v = i;
					best = dist[i];
				}
			}
			//cout << "v = " << v << endl;
			visited[v] = true;
			if (v == 1) break;
			for (int i = 0; i < n; i++){
				if (visited[i]) continue;
				int di = max(dist[v],calc_d(v,i));
				if (dist[i] > di){
					dist[i] = di;
				}
			}
			cnt++;
		}
		ld ans = dist[1];
		ans = sqrt(ans);
		printf("Case #%d: %.8f\n", zz, ans);
		//cout << "Case #" << zz << ": " << ans << endl;
	}
	
	return 0;
}
