#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int T, N, ans;
char skill[11][11];
int id[11], occ[11];

bool dfs2(int dep) {
	if(dep==N) return true;
	bool found = false;
	for(int i=0;i<N;i++)
		if(skill[id[dep]][i]=='1' && !occ[i]) {
			found = true;
			occ[i] = true;
			if (!dfs2(dep+1)) return false;
			occ[i] = false;
		}
	return found;
}

bool chk() {
	for(int i=0;i<N;i++) id[i] = i;
	memset(occ, false, sizeof occ);
	do {
		if (!dfs2(0)) return false;
	} while(next_permutation(id, id+N));
	return true;
}

void dfs(int worker, int machine, int spent) {
	if(worker == N) {
		if(chk()) ans=min(ans, spent);
		return;
	}
	
	int nxt_worker = worker, nxt_machine = machine;
	nxt_machine++;
	if(nxt_machine==N) {
		nxt_machine = 0;
		nxt_worker ++;
	}
	dfs(nxt_worker, nxt_machine, spent);
	if(skill[worker][machine] == '0') {
		skill[worker][machine] = '1';
		dfs(nxt_worker, nxt_machine, spent+1);
		skill[worker][machine] = '0';
	}
}

int main() {
	scanf("%d", &T);
	for(int CASE = 1; CASE <= T; CASE++) {
		scanf("%d", &N);
		for(int i=0;i<N;i++) scanf("%s", skill[i]);
		ans = N*N;
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", CASE, ans);
	}
	
	return 0;
}