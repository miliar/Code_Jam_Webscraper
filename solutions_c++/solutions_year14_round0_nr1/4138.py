#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,a,b,x=1,ans;
	int array1[4][4];
	int array2[4][4];
	freopen("A-small-attempt0.in","r",stdin);
	freopen("m.txt","w",stdout);
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&a);
		a--;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%d",&array1[i][j]);
			}
		}
		scanf("%d",&b);
		b--;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%d",&array2[i][j]);
			}
		}
		int tot = 0;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				if(array1[a][i]==array2[b][j]) {
					tot++;
					ans = array1[a][i];
				}
			}
		}
		if(tot==0) {
			printf("Case #%d: Volunteer cheated!\n",x++);
		}
		if(tot==1) {
			printf("Case #%d: %d\n",x++,ans);
		}
		if(tot>1) {
			printf("Case #%d: Bad magician!\n",x++);
		}
	}
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
