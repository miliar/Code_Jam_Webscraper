#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,test,n1,n2,v;
int a[5][5],b[5][5];
int main() {
	freopen("dash.in","r",stdin);
	freopen("dash.out","w",stdout);
	scanf("%d",&test);
	for (te=1;test;test--,te++) {
		scanf("%d",&n1);
		For(i,1,4)For(j,1,4) scanf("%d",&a[i][j]);
		scanf("%d",&n2);
		For(i,1,4)For(j,1,4) scanf("%d",&b[i][j]);
		k=0;
		For(i,1,4)For(j,1,4) if (a[n1][i]==b[n2][j]) k++,v=a[n1][i];
		printf("Case #%d: ",te);
		if (k==1) printf("%d\n",v);
		else if (k>1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	//for(;;);
	return 0;
}
