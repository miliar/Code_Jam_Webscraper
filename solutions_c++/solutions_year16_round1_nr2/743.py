#include <stdio.h>
#include <vector>
#include <algorithm>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int h[3000] = {0};
		int n;
		scanf("%d", &n);
		//std::vector<std::vector<int> > m;
		for (int i=0; i<n*2-1; i++) {
			//std::vector<int> v;
			for (int j=0; j<n; j++) {
				int a;
				scanf("%d", &a);
				h[a]++;
				//v.push_back(a);
			}
			//m.push_back(v);
		}
		std::vector<int> res;
		for (int i=0; i<3000; i++) {
			if (h[i]%2 == 1) {
				res.push_back(i);
			}
		}
		printf("Case #%d:", t);
		for (int i=0; i<(int)res.size(); i++) {
			printf(" %d", res[i]);
		}
		printf("\n");
		/*
		std::sort(m.begin(), m.end());
		int cur = 0;
		for (int i=0; i<n; i++) {
			if (cur >= n*2-1 || m[cur][0] != m[cur+1][0]) {
				cur++;
			} else {
				for (int j=0; j<i; j++) {
					r[][]
				}
				if (m[cur]) {
				}
				cur += 2;
			}
		}*/
	}
	return 0;
}