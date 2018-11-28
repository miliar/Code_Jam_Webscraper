#include <cstdio>
#include <vector>

using namespace std;

const int MAXH = 3E3;

int cnt[MAXH];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int n;
		scanf("%d", &n);
		for (int i = 2 * n - 2; i >= 0; --i){
			for (int t, j = 0; j < n; ++j){
				scanf("%d", &t);
				cnt[t] ^= 1;
			}
		}
		vector<int> ans;
		for (int i = 1; i < MAXH; ++i)
			if (cnt[i]){
				ans.push_back(i);
				cnt[i] = 0;
			}
		for (int i = 0; i < n; ++i)
			printf("%d%c", ans[i], "\n "[i < n - 1]);
	}
	return 0;
}
