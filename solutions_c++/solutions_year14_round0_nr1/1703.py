#include <cstdio>
int t,r1,r2,a[5],b[5],x,ans,n;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for (int T = 1;T <= t;T++){
		scanf("%d",&r1);
		for (int i = 1;i <= 4;i++)
			for (int j = 1;j <= 4;j++){
				scanf("%d",&x);
				if (i == r1) a[j] = x;
			}
		for (int i = 1;i <= 4;i++) b[i] = 0;
		scanf("%d",&r2);
		for (int i = 1;i <= 4;i++)
			for (int j = 1;j <= 4;j++){
				scanf("%d",&x);
				if (i == r2) for (int k = 1;k <= 4;k++) if (x == a[k]) b[k] = 1;
			}
		ans = n = 0;
		for (int i = 1;i <= 4;i++) if (b[i]){
			ans = a[i];
			n++;
		}
		printf("Case #%d: ",T);
		if (n == 1) printf("%d\n",ans);
		else if (n > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}
