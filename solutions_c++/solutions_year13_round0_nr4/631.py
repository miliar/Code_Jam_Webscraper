#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

int T,cs,K,n;

int keys[222];
int chest[222][222];
int open[222];
int tot_keys[1<<20][222];

map<int,int> id;
int m;

bool dp[1<<20];
bool ck[1<<20];
int dag[1<<20];

bool go(int mask) {
	if(mask == (1<<n) - 1) return 1;

	bool &ret = dp[mask];
	if(ck[mask]) return ret;
	ck[mask] = 1, ret = 0;

	for(int i=0;i<n;++i) {
		if(mask>>i & 1) continue;
		if(tot_keys[mask][open[i]] == 0) continue;
		bool tmp = go(mask | (1<<i));
		if(tmp) {
			ret = 1, dag[mask] = i;
			break;
		}
	} return ret;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;++cs) {
		memset(dag,-1,sizeof(dag));
		memset(ck,0,sizeof(ck));
		memset(keys,0,sizeof(keys));
		memset(chest,0,sizeof(chest));
		id.clear(), m = 0;
		memset(keys,0,sizeof(keys));
		scanf("%d%d",&K,&n);
		for(int i=0;i<K;++i) {
			int k; scanf("%d",&k);
			//keys[k]++;
			if(id.count(k) == 0) id[k] = m++; 
			keys[id[k]]++;
		}
		for(int i=0;i<n;++i) {
			int t,k; scanf("%d%d",&t,&k);
			if(id.count(t) == 0) id[t] = m++;
			open[i] = id[t];
			for(int j=0;j<k;++j) {
				int x; scanf("%d",&x);
				if(id.count(x) == 0) id[x] = m++;
				chest[i][id[x]]++;
			}
		}


		for(int i=0;i<(1<<n);++i) {
			for(int j=0;j<m;++j)
				tot_keys[i][j] += keys[j];
			for(int j=0;j<n;++j) {
				if(i>>j & 1) {
					for(int k=0;k<m;++k)
						tot_keys[i][k] += chest[j][k];
					tot_keys[i][open[j]]--;
				}
			}
		}

		bool ans = go(0);
		printf("Case #%d: ",cs);
		if(ans) {
			int mask = 0;
			while(dag[mask] != -1) {
				printf("%d ",dag[mask]+1);
				mask ^= (1<<dag[mask]);
			} puts("");
		}
		else {
			printf("IMPOSSIBLE\n");
		}

		for(int i=0;i<(1<<n);++i)
			for(int j=0;j<m;++j)
				tot_keys[i][j] = 0;
	}
	return 0;
}