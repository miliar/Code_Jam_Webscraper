#include<stdio.h>
int main() {
	int t,T,i,k,r,j,times[20],tmp;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		for(i=1;i<=16;i++) times[i]=0;
		for(k=0;k<2;k++) {
			scanf("%d",&r);
			for(i=1;i<=4;i++)
				for(j=0;j<4;j++) {
					scanf("%d",&tmp);
					if(i==r)
						times[tmp]++;
				}
		}
		tmp=0;
		for(i=1;i<=16;i++)
			if(times[i]==2) {
				if(tmp) break;
				else tmp=i;
			}
		if(i<=16) printf("Case #%d: Bad magician!\n",t);
		else if(tmp) printf("Case #%d: %d\n",t,tmp);
		else printf("Case #%d: Volunteer cheated!\n",t);
	}
	return 0;
}
