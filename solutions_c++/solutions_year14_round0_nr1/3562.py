#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;

int ccount[16];

int main(){
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i){
		memset(ccount, 0, sizeof(ccount));
		int resp[2];
		scanf("%d", &resp[0]);
		for (int n = 0; n < 4; ++n){
			for (int m = 0; m < 4; ++m){
				int q;
				scanf("%d", &q);
				if (n + 1 == resp[0])
					++ccount[q - 1];
			}
		}
		scanf("%d", &resp[1]);
		for (int n = 0; n < 4; ++n){
			for (int m = 0; m < 4; ++m){
				int q;
				scanf("%d", &q);
				if (n + 1 == resp[1])
					++ccount[q - 1];
			}
		}
		int tans = -1;
		bool bd = false;
		printf("Case #%d: ", i);
		for (int c = 0; c < 16; ++c){
			if (tans > -1 && ccount[c] == 2){
				printf("Bad magician!\n");
				bd = true;
				break;
			}
			if (ccount[c] == 2)
				tans = c + 1;
		}
		if (tans == -1)
			printf("Volunteer cheated!\n");
		else if (!bd)
			printf("%d\n", tans);
	}
	return 0;
}
