#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k,T,r1,ans,r2,M1[4][4],M2[4][4],count;
	scanf("%d",&T);
	for(k=1;k<=T;k++) {		// No of Test cases
	
		count = 0;
	
		// Take Input
		
		scanf("%d",&r1);
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%d",&M1[i][j]);
			}
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%d",&M2[i][j]);
			}
		}
		
		// Computing the number.
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				if(M1[r1-1][i]==M2[r2-1][j]) {
					count++;
					ans = M1[r1-1][i];
				}
			}
		}
		
		// Printing the result
		if(count==1) {
			printf("Case #%d: %d\n",k,ans);
		} else if(count>1) {
			printf("Case #%d: Bad magician!\n",k);
		} else {
			printf("Case #%d: Volunteer cheated!\n",k);
		}
	}
	return 0;
}
