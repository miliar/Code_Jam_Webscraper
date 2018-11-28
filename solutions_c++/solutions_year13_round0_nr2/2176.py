#include <cstdio>
#include <climits>
#include <algorithm>

int t, x[100][100], n, m, maxr[100], maxc[100];

using namespace std;

int main(){
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d%d", &n, &m);
		for (int j = 0; j < n; j++)
			for (int q = 0; q < m; q++)
				scanf("%d", &x[j][q]);
		
		fill(maxr, maxr + 100, INT_MIN);
		fill(maxc, maxc + 100, INT_MIN);
		
		for (int j = 0; j < n; j++)
			for (int q = 0; q < m; q++)
				maxr[j] = max(maxr[j], x[j][q]),
				maxc[q] = max(maxc[q], x[j][q]);
	
		bool p = true;
		for (int j = 0; j < n; j++)
			for (int q = 0; q < m; q++)
				if (maxr[j] > x[j][q] && maxc[q] > x[j][q])
					p = false;
		printf("Case #%d: %s\n", i + 1, ((p)?("YES"):("NO")));
	}
}
