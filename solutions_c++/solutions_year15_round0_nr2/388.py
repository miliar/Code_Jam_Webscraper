/*
 * ID: sfiction
 * COMP: GCJ
 * ROUND: Qualification
 * PROB: B
 */
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1E3 + 10;

int n;
int p[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		scanf("%d", &n);
		int high = 0;
		for (int i=0;i<n;++i){
			scanf("%d", &p[i]);
			high = max(high, p[i]);
		}

		int ans = high;
		for (int eat=high;eat>=1;--eat){
			int special = 0;
			for (int i=0;i<n;++i)
				special += (p[i] - 1) / eat;
			ans = min(ans, special + eat);
		}

		printf("Case #%d: %d\n", casi, ans);
	}
	return 0;
}
