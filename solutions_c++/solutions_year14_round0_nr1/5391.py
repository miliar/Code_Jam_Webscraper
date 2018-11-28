#include <cstdio>

using namespace std;

int A[4][4], B[4][4];

int erg[4];

int main() {

	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++) {
		printf("Case #%d:", t+1);
	
		int anz=0;
		int a, b;
		scanf("%d ", &a);
		for(int i=0; i<4; ++i) {
			for(int j=0; j<4; ++j) {
				scanf("%d ", &A[i][j]);
			}
		}
		scanf("%d ", &b);	 
		for(int i=0; i<4; ++i) {
			for(int j=0; j<4; ++j) {
				scanf("%d ", &B[i][j]);
				for(int k=0; k<4; ++k) {
					if(i+1==b) {
						if(B[i][j]==A[a-1][k]) {
							erg[anz++] = B[i][j];
						}
					}
				}
			}
		}
		
		if(anz==0) {
			printf(" Volunteer cheated!\n");
		} else if(anz>1) {
			printf(" Bad magician!\n");
		} else {
			for(int i=0; i<anz; i++){
				printf(" %d", erg[i]); 
			}
			printf("\n");
		}
		
	}
	
	return 0;
}
