/*
 * ID: sfiction
 * COMP: GCJ
 * ROUGN: Qualification
 * PROB: A
 */
#include <cstdio>

const int MAXN = 1E3 + 10;

int n;
char str[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		scanf("%d", &n);
		scanf("%s", str);

		int stand = 0, invite = 0;
		for (int i=0;i<=n;++i){
			if (stand < i){
				invite += i - stand;
				stand = i;
			}
			stand += str[i] - '0';
		}

		printf("Case #%d: %d\n", casi, invite);
	}
	return 0;
}
