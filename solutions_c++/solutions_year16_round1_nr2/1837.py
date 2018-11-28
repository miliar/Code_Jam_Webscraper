#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int cnt[2504];
	for(int NOWCASE=1; NOWCASE<=T; ++NOWCASE) {
		int N;
		scanf("%d", &N);
		memset(cnt, 0, sizeof(cnt));
		for(int i=2*N-1; i>0; --i)
			for(int j=0,v; j<N; ++j) {
				scanf("%d", &v);
				++cnt[v];
			}
		vector<int> ans;
		for(int i=1; i<=2500; ++i)
			if( cnt[i]&1 )
				ans.emplace_back(i);
		printf("Case #%d:", NOWCASE);
		for(int i=0; i<ans.size(); ++i)
			printf(" %d", ans[i]);
		puts("");
	}
	return 0;
}
