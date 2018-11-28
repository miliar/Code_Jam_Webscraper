#include <cstdio>
#include <algorithm>
#include <map>
#define N 1010
#define INF 2147483647

using namespace std;

int a[N], b[N];
map<int, int> p;

int main(){
	int T, cas, n, i, j, ans, tmp;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		scanf("%d" ,&n);
		p.clear();
		for (i = 0; i < n; i++){
			scanf("%d", &a[i]);
			p[a[i]] = i;
		}
		sort(a, a+n);
		ans = INF;
		do{
			for (i = 0; i < n-1 && a[i] < a[i+1]; i++);
			for (; i < n-1 && a[i] > a[i+1]; i++);
			if (i != n-1) continue;
			for (i = 0; i < n; i++)
				b[p[a[i]]] = i;
			tmp = 0;
			for (i = 0; i < n-1; i++)
				for (j = i+1; j < n; j++)
					if (b[i] > b[j])
						tmp++;
			ans = min(ans, tmp);
		}while (next_permutation(a, a+n));
		printf("Case #%d: %d\n", cas, ans);
	}
}

