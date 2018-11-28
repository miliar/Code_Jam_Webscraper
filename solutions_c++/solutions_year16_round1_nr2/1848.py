#include <cstdio>
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <vector>
using std::vector;
#include <algorithm>
using std::sort;

int tmp, list[2500], nlist[2500];
vector<int> ans;
int main()
{
	int T;	scanf("%d", &T);
	for(int i = 0; i < T; ++i) {
		int N;	scanf("%d", &N);
		scanf("%d", &list[0]);
		nlist[0] = 1;
		int k = 0;
		int num = 2 * N * N - N;
		for(int j = 1; j < num; ++j) {
			scanf("%d", &tmp);
			int done = 0;
			for(int l = 0; l <=k; ++l)
				if(list[l] == tmp) {
					++nlist[l];
					done = 1;
					break;
				}
			if(!done) {
				++k;
				list[k] = tmp;
				nlist[k] = 1;
			}
		}
		for(int j = 0; j <=k; ++j)
			if(nlist[j] % 2)
				ans.push_back(list[j]);
		sort(ans.begin(), ans.end());
		printf("Case #%d: ", i + 1);
		for(int j = 0; j < ans.size(); ++j) {
			cout << ans[j] << ' ';
		}
		puts("");
		ans.clear();
	}
	return 0;
}
