#include <cstdio>

int T, f, num, ans;
int a[20];

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++Case) {
		for (int i = 1; i <= 16; ++i)
		  a[i] = 0;
		ans = -1;
	  scanf("%d", &f);
	  for (int i = 1; i <= 4; ++i)
	    for (int j = 1; j <= 4; ++j) {
			  scanf("%d", &num);
			  if (i == f)
			    a[num]++;
			}
	  scanf("%d", &f);
		for (int i = 1; i <= 4; ++i)
		  for (int j = 1; j <= 4; ++j) {
			  scanf("%d", &num);
			  if (i == f)
			    a[num]++;
			}
		for (int i = 1; i <= 16; ++i)
		  if (a[i] == 2)
		    ans = (ans == -1 ? i : -2);
		printf("Case #%d: ", Case);
		if (ans == -1) {
			printf("Volunteer cheated!\n");
		} else if (ans == -2) {
			printf("Bad magician!\n");
		} else {
		  printf("%d\n", ans);
		}
	}
	return 0;
}
