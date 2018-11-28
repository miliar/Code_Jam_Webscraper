#include<cstdio>
#include<algorithm>
#include<deque>
using namespace std;
typedef long long i64;

int T;
int E, R, N, V[30000];

/*
i64 solve(int left, int right, int init)
{
	//Žg‚¢‚«‚Á‚Ä‚µ‚Ü‚Á‚Ä‚æ‚¢‚È‚Ì
	if(left >= right) return 0;

	pair<int, int> mxp = make_pair(-1, -1);
	for(int i=left;i<right;i++){
		mxp = max(mxp, make_pair(V[i], i));
	}

	if(init + (i64)R * (mxp.second - left) <= E){
		return V[mxp.second] * (init + (i64)R * (mxp.second - left)) + solve(mxp.second+1, right, R);
	}else{
		int mx2 = -1, ne = E;
		for(int i=mxp.second-1;i>=left;i--){
			ne -= R;
			mx2 = max(mx2, V[i]);
			if(ne <= R){
				return (R-ne) * (i64)mx2 + (V[mxp.second] * E + solve(mxp.second+1, right, R)) + solve(left, i, init);
			}
		}

		//return solve(left+1, right, init) + V[left] * R;
		for(int i=left+1;i<=mxp.second;i++){
			if(V[left] <= V[i]){
				return (i-left) * R * V[left] + solve(i, right, init);
			}
		}
	}
	return -1;
}
*/

int cnt[30000], last;

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%d%d%d", &E, &R, &N);
		for(int i=0;i<N;i++) scanf("%d", V+i);
		for(int i=0;i<N;i++) cnt[i] = -1;
		cnt[0] = E;
		last = 0;

		deque<int> Q;
		i64 ret = 0;
		R = min(R, E);
		for(int i=0;i<N;i++){
			
			//printf("%d %lld %d\n", i, ret, cnt[last]);
			while((i64)cnt[last] + (i64)(i - last) * R > E){
				i64 ext = cnt[last] + (i64)(i - last) * R - E;
				//printf("%lld %d\n", ext, last);
				if(cnt[last] >= ext){
					ret += (i64)ext * V[last];
					cnt[last] -= ext;
					break;
				}else{
					ret += (i64)cnt[last] * V[last];
					ext -= cnt[last];
					cnt[last] = 0;
					Q.pop_front();
					while(last < Q[0]){
						cnt[last+1] = cnt[last] + R; last++;
					}
				}
			}
			if(i==N) break;
			while(!Q.empty() && V[Q[Q.size()-1]] < V[i]){
				Q.pop_back();
			}
			Q.push_back(i);

			while(!Q.empty() && last < Q[0]){
				cnt[last+1] = cnt[last] + R; last++;
			}

		}
			while(cnt[last] + (N-1 - last) * R > 0){
				int ext = cnt[last] + (N-1 - last) * R;
				if(cnt[last] >= ext){
					ret += (i64)ext * V[last];
					cnt[last] -= ext;
				}else{
					ret += (i64)cnt[last] * V[last];
					ext -= cnt[last];
					cnt[last] = 0;
					Q.pop_front();
					while(last < Q[0]){
						cnt[last+1] = cnt[last] + R; last++;
					}
				}
			}

		printf("Case #%d: %lld\n", t, ret);
	}

	return 0;
}
