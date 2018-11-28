#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int t,n,k,i,j;
double p[205],ans,val[1 << 20 + 5];
bool used[205],used1[205];
vector <int> YES,NO;

void solve_NO(int id, int pick, double temp, double temp1, int mask){
	if(id == n){
		if(pick == k / 2){
			val[mask] += temp * temp1;
			ans = max(ans, val[mask]);
		}
		return;
	}
	solve_NO(id + 1, pick, temp, temp1, mask);
	if(!used[id]){
		used1[id] = 1;
		solve_NO(id + 1, pick + 1, temp * (1.0 - p[id]), temp1, mask + (1 << id));
		used1[id] = 0;
	}
}

void solve_YES(int id, int pick){
	if(id == n){
		if(pick == k / 2){
			YES.clear();
			double now = 1.0;
			int tot = 0;
			for(int k = 0; k < n; k++){
				if(used[k]){
					YES.push_back(k);
					now *= p[k];
					tot += (1 << k);
				}
			}
			solve_NO(0, 0, 1.0, now, tot);
		}
		return;
	}
	solve_YES(id + 1, pick);
	used[id] = 1;
	solve_YES(id + 1, pick + 1);
	used[id] = 0;
}

int main(){
	scanf("%d", &t);
	int testcase = 0;
	while(++testcase <= t){
		memset(val, 0, sizeof(val));
		scanf("%d%d", &n, &k);
		for(i = 0; i < n; i++)
		scanf("%lf", &p[i]);
		ans = 0.0;
		solve_YES(0, 0);
		printf("Case #%d: %.12lf\n", testcase, ans);
	}	
}

