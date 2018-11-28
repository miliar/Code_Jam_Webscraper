#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int S[10001];
int main(){
	freopen("P1.in", "r", stdin);
	freopen("P1.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
		int n, sz;
		scanf("%d%d", &n, &sz);
		for (int i = 0; i < n; i++){
			scanf("%d", S + i);
		}
		sort(S, S + n);
		int L = 0, R = n - 1;
		int cnt = 0;
		while (L <= R){
			if (L == R){
				cnt++;
				break;
			}
			if (S[L] + S[R] <= sz){
				cnt++, L++, R--;
			}
			else {
				cnt++, R--; 
			}
		}
		printf("%d\n", cnt);
	}
}
