#include <stdio.h>
#include <string.h>

int main(){
	//freopen("
	int T;
	scanf("%d",&T);
	
	
	for(int i=0;i<T;++i){
		int pos[16] = {0};
		
		int n;
		scanf("%d",&n);
		for(int j=0;j<4;++j){
			int tmp;
			for(int k=0;k<4;++k){
				scanf("%d",&tmp);
				if( j == n-1 ) ++pos[tmp-1];
			}
		}
		scanf("%d",&n);
		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k){
				int tmp;
				scanf("%d",&tmp);
				if( j == n-1 ) ++pos[tmp-1];	
			}
		//for(int j=0;j<16;++j)
		//	printf("%d ", pos[j]);
		//printf("\n");
		int cnt = 0;
		int last = 0;
		for(int j=0;j<16;++j)
			if( pos[j] == 2) ++cnt, last = j;
		printf("Case #%d: ",i+1);
		if( cnt == 0 )
			printf("Volunteer cheated!\n");
		else if (cnt > 1 )
			printf("Bad magician!\n");
		else printf("%d\n", last+1);
	}
	
	return 0;	
}
