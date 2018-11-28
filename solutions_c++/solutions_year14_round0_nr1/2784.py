#include <stdio.h>

int main(void) {
	int t,a1,a2,p[4][4],q[4][4];
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		int count=0,ans;
		scanf("%d",&a1);
		for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&p[i][j]);
        scanf("%d",&a2);
		for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&q[i][j]);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(p[a1-1][i]==q[a2-1][j]){
					++count;
					ans=p[a1-1][i];
				}
			}
		}
		if(count==1) printf("Case #%d: %d\n",k+1,ans);
		else if(count==0) printf("Case #%d: Volunteer cheated!\n",k+1);
		else printf("Case #%d: Bad magician!\n",k+1);
	}
	return 0;
}
