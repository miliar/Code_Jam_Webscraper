#include<stdio.h>
int a[10],x,r1,r2,tc;
int main() {
	freopen("A.in","r",stdin);                    
	freopen("A.out","w",stdout);  
	scanf("%d",&tc);
	for (int t=1;t<=tc;t++) {
		int answer=0,ans=0;
		printf("Case #%d: ",t);
		scanf("%d",&r1);
		for (int i=1;i<=4;i++) {
			for (int j=1;j<=4;j++) {
				if (i==r1) scanf("%d",&a[j]);
				else scanf("%d",&x);
			}
		}
		scanf("%d",&r2);
		for (int i=1;i<=4;i++) {
			for (int j=1;j<=4;j++) {
				scanf("%d",&x);				
				if (r2==i) {
					for (int k=1;k<=4;k++) {
						if (a[k]==x) {ans++; answer=x; break;}
					}
				}
			}
		}
		if (ans>1) printf("Bad magician!\n");
		if (ans==0) printf("Volunteer cheated!\n");
		else if (ans==1) printf("%d\n",answer);
	}
}
