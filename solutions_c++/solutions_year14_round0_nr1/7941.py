#include <stdio.h>
int main(){
	int t;
	int pre[4][4], nxt[4][4];
	scanf("%d", &t);
	for(int i=0;i<t;++i){
		int r_pre, r_nxt;
		scanf("%d", &r_pre);
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k)
				scanf("%d", &pre[j][k]);
		scanf("%d", &r_nxt);
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k)
				scanf("%d", &nxt[j][k]);
				
		int cnt = 0, record;
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k)
				if(pre[r_pre-1][j] == nxt[r_nxt-1][k]){
					++cnt;
					record = pre[r_pre-1][j];
				}
		printf("Case #%d: ", i+1);
		if(cnt == 1) 	 printf("%d\n", record);
		else if(cnt > 1) printf("Bad magician!\n");
		else			 printf("Volunteer cheated!\n");
	}
}
