#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int row[4] = {0};

int cmp ( const void *a , const void *b ){
	return *(int *)a - *(int *)b;
}

int min(int a, int b){return a<b?a:b;}

int main(){

   freopen("A-small-attempt0.in", "r", stdin);
   freopen("test.txt", "w", stdout);
	
//	qsort(map,n,sizeof(map[0]),cmp);
//	memset(map,0,sizeof(map));
	int t, i, j, r, p, q, count, ans, tp;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		count = 0;
		scanf("%d", &r);
		for(j=1; j<=4; j++){
			if(r == j){
				for(p=0; p<4; p++){
					scanf("%d",&row[p]);
				}
			}else{
				for(p=0; p<4; p++){
					scanf("%d",&tp);
				}
			}
		}
		scanf("%d", &r);
		for(j=1; j<=4; j++){
			if(r == j){
				for(p=0; p<4; p++){
					scanf("%d",&tp);
					for(q=0; q<4; q++){
						if(tp == row[q]){
							ans = tp;
							count++;
						}
					}
				}
			}else{
				for(p=0; p<4; p++){
					scanf("%d",&tp);
				}
			}
		}
		printf("Case #%d: ",i+1);
		if(count == 0){
			printf("Volunteer cheated!\n");
		}else if(count == 1){
			printf("%d\n",ans);
		}else{
			printf("Bad magician!\n");
		}

	}
	return 0;
}