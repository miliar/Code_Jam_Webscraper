//LANG:C++
#include <cstdio>
#include <cstring>

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t, row1, row2, in, num[16]={0}, ans=-1;
	scanf("%d", &t);
	for (int a=0; a<t; a++) {
		memset(num, 0, sizeof(num));
		ans=-1;
		scanf("%d", &row1);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d", &in);
				if (i+1 == row1) num[in-1]++;
			}
		}
		scanf("%d", &row2);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d", &in);
				if (i+1 == row2 && num[in-1] == 1)  {
					if (ans != -1) ans = -2;
					if (ans == -1) ans = in;
				}
			}
		}
		printf("Case #%d: ", a+1);
		if(ans == -1) printf("Volunteer cheated!\n");
		else if(ans == -2) printf("Bad magician!\n");
		else printf("%d\n", ans);
	}
}
