#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

const int MAXN = 1000005;

long long cnt[MAXN];
int A[MAXN];
int cases, N, p, q, r, s;

int main(){
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
		for(int i = 0; i < N; ++i){
			A[i] = ((i * p + q) % r + s);
			if(i != 0) cnt[i] = cnt[i - 1] + A[i];
			else cnt[i] = A[i];
		}
		long long tot = cnt[N - 1];
		long long gao = tot / 3;
		//printf("%I64d %I64d\n", tot, gao);
		long long now = 0;
		long long ans = 0;
		vector<int> checkPt;
		for(int i = 0; i < N; ++i){
			now = now + A[i];
			if(now > gao){
				checkPt.push_back(i);
				//printf("gao->%d\n", i);
				now = 0;
			}
		}
		if(checkPt.size() == 0){
			assert(false);
		} else if(checkPt.size() == 1){
			ans = tot - cnt[checkPt[0]];
		} else {
			long long tmp = 1LL << 62;
			for(int i = checkPt[0] - 10; i <= checkPt[0] + 10; ++i)
				if(i >= 0 && i <= N - 1)
					for(int j = checkPt[1] - 10; j <= checkPt[1] + 10; ++j)
						if(j >= 0 && j <= N - 1 && i <= j){
							//printf("%d %d %I64d %I64d %I64d\n", i, j, cnt[i], cnt[j] - cnt[i], tot - cnt[j]);
							tmp = min(tmp, max(max(cnt[j] - cnt[i], cnt[i]), tot - cnt[j]));
						}
			//printf("%I64d\n", tmp);
			ans = tot - tmp;
		}
		printf("Case #%d: %.10lf\n", xx, ans * 1.0 / tot);
	}
}
