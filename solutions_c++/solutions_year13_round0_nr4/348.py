#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int T, K, N;
bool able[1<<20];
int req[21], next[1<<20];
vector<int> keys[21];

int main()
{
	int in, sz;
	int kcnt[201];
	scanf("%d", &T);
	for(int t=0;t++<T;){
		for(int i=0;i<=200;i++) kcnt[i] = 0;

		scanf("%d%d", &K, &N);
		for(int i=0;i<=N;i++) keys[i].clear();
		for(int i=0;i<K;i++){
			scanf("%d", &in); keys[N].push_back(in);
		}
		req[N] = 0;
		for(int i=0;i<N;i++){
			scanf("%d%d", req+i, &sz);
			for(int j=0;j<sz;j++){
				scanf("%d", &in); keys[i].push_back(in);
			}
		}

		for(int i=0;i<(1<<N);i++){
			able[i] = false; next[i] = 0;
		}

		for(int i=0;i<(1<<N);i++){
			for(int j=0;j<=N;j++) if(j==N || (i&(1<<j))){
				kcnt[req[j]]--;
				for(int k=0;k<keys[j].size();k++) kcnt[keys[j][k]]++;
			}
			for(int j=0;j<N;j++) if(!(i&(1<<j)) && kcnt[req[j]]){
				next[i] |= 1<<j;
			}

			for(int j=0;j<=N;j++) if(j==N || (i&(1<<j))){
				kcnt[req[j]]++;
				for(int k=0;k<keys[j].size();k++) kcnt[keys[j][k]]--;
			}
		}

		able[(1<<N)-1] = true;
		for(int i=(1<<N)-2;i>=0;i--){
			for(int j=0;j<N;j++) if((next[i] & (1<<j))) able[i] |= able[i | (1<<j)];
		}
		printf("Case #%d:", t);

		if(!able[0]) puts(" IMPOSSIBLE");
		else{
			int ps = 0;
			while(ps != (1<<N)-1){
				for(int j=0;j<N;j++) if(next[ps] & (1<<j)){
					if(able[ps | (1<<j)]){
						printf(" %d", j+1);
						ps |= 1<<j;
						break;
					}
				}
			}
			puts("");
		}
	}

	return 0;
}
