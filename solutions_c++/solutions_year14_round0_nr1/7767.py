#include<stdio.h>
int main()
{
	int t, c = 1;
	scanf("%d",&t);
	while (t--) {
		int a[4][4], r1, r2, f = -1, no, count[17] = {0}, i, j, a2[4][4];
		scanf("%d",&r1);
		r1--;
		for(i = 0; i < 4; i++) {
			
			for(j = 0; j < 4; j++) {
				scanf("%d",&a[i][j]);
				if(i == r1)
				count[a[i][j]]++;
			}
		}
		scanf("%d",&r2);
		r2--;
			for(i = 0; i < 4; i++) {
			
			for(j = 0; j < 4; j++) {
				scanf("%d",&a2[i][j]);
				if(i == r2)
				count[a2[i][j]]++;
			}
		}
		for(i = 0; i < 17; i++) {
			if(f == -1) {
				if(count[i] == 2) no = i, f = 0;
			}
			else if (f == 0)
				if(count[i] == 2) f = 1;
		}
		freopen("output.txt","w",stdout);
		if (f ==0) printf("Case #%d: %d\n",c++,no);
		else if(f == 1) printf("Case #%d: Bad magician!\n",c++);
		else if (f == -1) printf("Case #%d: Volunteer cheated!\n",c++);
	}
	return 0;
}
