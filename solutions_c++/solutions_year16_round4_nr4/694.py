#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using std::min;
using std::vector;
using std::next_permutation;

int a[4][4];
int T, N;
char in[10];
int ans; 

vector<int> lst;
bool used[4];

bool dfs_test(int ni) {
	if(ni == N) return true;
	int now = lst[ni];
	int cnt = 0;
	for(int i=0; i<N; i++) {
		if(used[i] || !a[now][i]) continue;
		cnt ++;
		used[i] = true;
		//printf("%d choost %d\n", now, i);
		if(!dfs_test(ni+1)) return false;
		used[i] = false;
	}
	//printf("%d: cnt=%d\n", now, cnt);
	return cnt > 0;
}

bool valid() {
	lst = vector<int>();
	for(int i=0; i<N; i++) lst.push_back(i);
	do {
		memset(used, 0, sizeof(used));
		/*printf(">>>");
		for(int i=0; i<N; i++) printf("%d", lst[i]);
		puts("");*/
		if(!dfs_test(0)) return false;
	} while( next_permutation(lst.begin(), lst.end()) );
	return true;
}

void dfs(int i, int j, int now) {
	//if(now > ans) return;
	if(i==N && j==0) {
		if(valid()) {
			/*for(int ii=0; ii<N; ii++, puts(""))
				for(int jj=0; jj<N; jj++)
					printf("%d", a[ii][jj]);
			printf("===%d\n", now);*/
			ans = min(ans, now);
		}
		return ;
	}
	int ni, nj;
	if(j==N-1) {ni=i+1; nj=0;}
	else {ni=i; nj=j+1;}
	if(a[i][j] == 1) dfs(ni, nj, now);
	else {
		dfs(ni, nj, now);
		a[i][j] = 1;
		dfs(ni, nj, now+1);
		a[i][j] = 0;
	}
	return ;
}

int main() {
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d", &N);
		for(int i=0; i<N; i++) {
			scanf("%s", in);
			for(int j=0; j<N; j++) a[i][j] = (in[j]-'0');
		}
		ans = N*N;
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
