#include <cstdio>

using namespace std;

int main(){
	int T,r1,r2,A[4][4],B[4][4];
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d",&r1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&A[j][k]);
		scanf("%d",&r2);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&B[j][k]);
		int *C = A[r1-1];
		int *D = B[r2-1];
		int count = 0;
		int card;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(C[j]==D[k]){
					count++;
					card = C[j];
				}
			}
		}
		if(count == 0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else if (count == 1)
			printf("Case #%d: %d\n",i+1,card);
		else
			printf("Case #%d: Bad magician!\n",i+1);
	}
	return 0;
}
