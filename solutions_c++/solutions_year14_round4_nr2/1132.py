#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;
int S[1111];
int A[1111], B[1111], C[1111];
int calc(int n){
	int cost = 0;
	for (int i = n - 1; i >= 0; i--)
		for (int j = 0; j < i; j++)
			if (B[j] > B[j + 1]){
				swap(B[j], B[j + 1]);
				cost++;
			}
	return cost;
}
int main(){
	freopen("P2.in", "r", stdin);
	freopen("P2.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
		int n; scanf("%d", &n);
		map<int,int> mp;
		for (int i = 0; i < n; i++){
			scanf("%d", S + i);
			A[i] = B[i] = C[i] = S[i];
		}
		for (int i = 0; i < n; i++)
			mp[S[i]] = i;
		for (int i = 0; i < n; i++)
			S[i] = B[i] = mp[S[i]];
		int minAns = 0x7fffffff;
		sort(C, C + n);
		for (int i = 0; i < n; i++){

		}
		printf("%d\n", minAns);
	}
}
//permutation