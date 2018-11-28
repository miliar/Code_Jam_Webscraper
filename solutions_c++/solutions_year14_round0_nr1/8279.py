#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int t1[4][4];
int t2[4][4];
int mark[17];

int main(){
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t){
		int a1, a2;
		scanf("%d", &a1);
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &t1[i][j]);
			}
		}
		scanf("%d", &a2);
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &t2[i][j]);
			}
		}
		memset(mark, 0, sizeof(mark));
		a1--; a2--;
		for (int i = 0; i < 4; ++i){
			mark[t1[a1][i]]++;
			mark[t2[a2][i]]++;
		}
		printf("Case #%d: ", t);
		int a = 0, b = 0, c = 0, n;
		for (int i = 1; i < 17; ++i){
			if (mark[i] == 0)a++;
			else if (mark[i] == 1)b++;
			else if (mark[i] == 2){
				if (c == 0)n = i;
				c++;
			}
		}

		if (c == 1)
			printf("%d\n", n);
		else if (c > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");

	}
	return 0;
}
