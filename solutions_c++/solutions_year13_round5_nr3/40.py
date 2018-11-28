#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstdlib>
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;
typedef vector<i64> llvec;
typedef unsigned int uint;

int T, u[1000], v[1000], a[1000], b[1000];
int N, M, P, path[500];
vector<pair<int, int> > cost[1000]; ivec dest[1000];

bool vis[1000];

int main()
{
	scanf("%d", &T);

	for(int t=0;t++<T;){
		scanf("%d%d%d", &N, &M, &P);
		for(int i=0;i<N;i++){
			cost[i].clear(); dest[i].clear();
		}

		for(int i=0;i<M;i++){
			scanf("%d%d%lld%lld", u+i, v+i, a+i, b+i);
			--u[i]; --v[i];
			cost[u[i]].push_back(make_pair(a[i], b[i]));
			dest[u[i]].push_back(v[i]);
			cost[v[i]].push_back(make_pair(a[i], b[i]));
			dest[v[i]].push_back(u[i]);
		}

		for(int i=0;i<P;i++){
			scanf("%d", path+i); path[i]--;
		}

		int ret = -1;
		for(int i=0;i<P;i++){
			//check

			for(int j=0;j<N;j++) vis[j] = false;

			priority_queue<pair<int, int> > Q;
			uint sum=0;
			for(int j=0;j<=i;j++){
				//printf("%d %d\n", sum, u[path[j]]);
				Q.push(make_pair(-sum, ~(u[path[j]])));
				sum += a[path[j]];
			}
			Q.push(make_pair(-sum, v[path[i]]));

			bool flg = false;

			while(!Q.empty()){
				pair<int, int> tmp = Q.top(); Q.pop();
				//printf("%d %d %d\n", i, tmp.first, tmp.second);
				int ps = tmp.second;

				if(ps < 0){
					ps = ~ps;
					if(vis[ps]) continue;
					vis[ps] = true;

					for(int j=0;j<cost[ps].size();j++){
						Q.push(make_pair(tmp.first - cost[ps][j].second, ~dest[ps][j]));
					}

					continue;
				}

				if(vis[ps]) continue;

				if(ps == 1){
					flg = true;
					break;
				}

				vis[ps] = true;

				for(int j=0;j<cost[ps].size();j++){
					Q.push(make_pair(tmp.first - cost[ps][j].first, dest[ps][j]));
				}
			}

			if(!flg){
				ret = path[i] + 1;
				break;
			}
		}

		if(ret==-1) printf("Case #%d: Looks Good To Me\n", t);
		else printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}
