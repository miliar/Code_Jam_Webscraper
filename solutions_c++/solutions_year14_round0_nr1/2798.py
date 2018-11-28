#include <cstdio>
#include <cstring>

using namespace std;

int p,q;
int a[4][4];
int b[4][4];
int ans;

int main() {
	int t,i,j,k,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		ans=-1;
		scanf("%d",&p);
		for (i=0;i<4;i++) 
			for (j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&q);
		for (i=0;i<4;i++) 
			for (j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		p--;q--;
		//for (i=0;i<4;i++) 
			//printf("%d ",a[p][i]);
		//printf("\n");
		//for (i=0;i<4;i++) 
			//printf("%d ",b[q][i]);
		//printf("\n");
		for (i=0;i<4;i++) 
			for (j=0;j<4;j++)
				if (a[p][i]==b[q][j]) {
					if (ans==-1) ans=a[p][i];
					else ans=-2;
				}
		printf("Case #%d: ",tt);
		if (ans==-1) printf("Volunteer cheated!\n");
		else if (ans==-2) printf("Bad magician!\n");
		else printf("%d\n",ans);
	}
	return 0;
}
