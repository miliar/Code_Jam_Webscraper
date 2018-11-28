/*
 * ID: sfiction
 * COMP: GCJ
 * ROUND: Round 1A
 * PROB: A
 */
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1E3 + 10;

int n;
int a[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		scanf("%d", &n);
		for (int i=0;i<n;++i)
			scanf("%d", &a[i]);

		int ansa = 0;
		int maxNum = 0;
		for (int i=1;i<n;++i)
			if (a[i] < a[i - 1]){
				ansa += a[i - 1] - a[i];
				maxNum = max(maxNum, a[i - 1] - a[i]);
			}

		int ansb = 0;
		for (int i=0;i<n-1;++i)
			ansb += min(maxNum, a[i]);

		printf("Case #%d: %d %d\n", casi, ansa, ansb);
	}
	return 0;
}
