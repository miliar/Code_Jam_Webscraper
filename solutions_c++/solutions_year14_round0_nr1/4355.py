#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t, x = 1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("m1.txt","w",stdout);
	scanf("%d", &t);
	while(t--) {
		int r1, r2, i, j, c = 0, p;
		scanf("%d", &r1);
		int a1[4][4], a2[4][4];
		for(i = 0; i <4; i++) {
			for(j = 0; j < 4; j++) {
				scanf("%d", &a1[i][j]);
			}
		}
		scanf("%d", &r2);
		
		for(i = 0; i <4; i++) {
			for(j = 0; j < 4; j++) {
				scanf("%d", &a2[i][j]);
			}
		}
		r1--;
		r2--;
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				if(a1[r1][i] == a2[r2][j]) {
				
					c++;
					p = i;
				}
			}
		}
		if(c == 1) 
			printf("Case #%d: %d\n", x++, a1[r1][p]);
		else if(c == 0) 
			printf("Case #%d: Volunteer cheated!\n", x++);
			else 
				printf("Case #%d: Bad magician!\n", x++);	
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
