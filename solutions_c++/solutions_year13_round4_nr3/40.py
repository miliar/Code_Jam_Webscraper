#include <cstdio>
#include <vector>
#include <queue>

int cnt[2010];
std::vector<int> edge[2010];

int main(){

	int T;
	scanf("%d" ,&T);

	for(int t = 1; t <= T; t++){
		printf("Case #%d: " ,t);

		int n;
		scanf("%d" ,&n);

		for(int i = 1; i <= n; i++){
			cnt[i] = 0;
			edge[i].clear();
		}

		int num[2010], lst[2010];
		for(int i = 1; i <= n; i++) scanf("%d" ,&num[i]);
		for(int i = 1; i <= n; i++){
			lst[num[i]] = i;
			for(int j = 1; j < i; j++){
				if(num[j] >= num[i]) edge[j].push_back(i), cnt[i]++;
			}
			if(num[i] > 1) edge[i].push_back(lst[num[i] - 1]), cnt[lst[num[i] - 1]]++;
		}

		for(int i = 1; i <= n; i++) scanf("%d" ,&num[i]);
		for(int i = n; i >= 1; i--){
			lst[num[i]] = i;
			for(int j = i + 1; j <= n; j++){
				if(num[j] >= num[i]) edge[j].push_back(i), cnt[i]++;
			}
			if(num[i] > 1) edge[i].push_back(lst[num[i] - 1]), cnt[lst[num[i] - 1]]++;
		}

		int idx = n;
		int ans[2010];
		std::priority_queue<int> heap;
		for(int i = 1; i <= n; i++){
			if(cnt[i] == 0) heap.push(i);
		}
		while(idx > 0){

			int now = heap.top(); heap.pop();
			ans[now] = idx--;

			for(int i = 0; i < edge[now].size(); i++){
				if(--cnt[edge[now][i]] == 0) heap.push(edge[now][i]);
			}

		}

		for(int i = 1; i <= n; i++){
			printf("%d%c" ,ans[i] ,i == n? '\n': ' ');
		}

	}

}
