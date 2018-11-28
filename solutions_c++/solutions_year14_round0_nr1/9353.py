#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int ag[4][4], t1[4], t2[4], T, aw;

int main() {
	//freopen("D://A-small-attempt1.in", "r", stdin);
	//freopen("D://A-small-attempt1.out", "w", stdout);
	scanf("%d", &T);
	for (int id = 1; id <= T; ++id) {
		int t = 0, x;
		scanf("%d", &aw);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", ag[i] + j);
		memcpy(t1, ag[0] + (aw - 1) * 4, sizeof(t1));
		scanf("%d", &aw);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", ag[i] + j);
		memcpy(t2, ag[0] + (aw - 1) * 4, sizeof(t1));
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j)
				if (t1[i] == t2[j]) {
					t++;
					x = t1[i];
				}
		}
		printf("Case #%d: ", id);
		switch(t) {
		case 0:
			printf("Volunteer cheated!\n");
			break;
		case 1:
			printf("%d\n", x);
			break;
		default:
			printf("Bad magician!\n");
		}
	}
	return 0;
}
