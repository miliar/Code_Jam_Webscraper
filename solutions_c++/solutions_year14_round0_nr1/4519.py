#include <cstdio>
#include <cstdlib>

int i,j,x,y,t,tes,ans;
int ctr[20];

int main() {
	scanf("%d",&t);
	for (tes=1; tes<=t ; tes++) {
		for (i=1 ; i<=16 ; i++) ctr[i] = 0;
		
		scanf("%d",&x);
		for (i=1 ; i<=4 ; i++)
			for (j=1 ; j<=4 ; j++) {
				scanf("%d",&y);
				if (i == x) ctr[y]++;
			}
			
		scanf("%d",&x);
		for (i=1 ; i<=4 ; i++)
			for (j=1 ; j<=4 ; j++) {
				scanf("%d",&y);
				if (i == x) ctr[y]++;
			}
			
		ans = -1;
		for (i=1 ; i<=16 ; i++) {
			if (ctr[i] == 2) {
				if (ans == -1) ans = i; else ans = -2;
			}
		}
		
		printf("Case #%d: ",tes);
		if (ans == -2) printf("Bad magician!\n"); else
		if (ans == -1) printf("Volunteer cheated!\n"); else
		printf("%d\n",ans);
	}
}