#include<cstdio>
#include<algorithm>
using namespace std;
int A[10][10];
int B[10][10];
int main(){
	int t;
	scanf("%d", &t);
	for( int k=0;k<t;k++){
		int r1, r2;
		scanf("%d", &r1);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				scanf("%d", &A[i][j]);
		}
		scanf("%d", &r2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				scanf("%d", &B[i][j]);
		}
		int last;
		int cont=0;
		r1--;
		r2--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(A[r1][i] == B[r2][j]){
					cont++;
					last=A[r1][i];
				}
			}
		}
		if(cont==0){
			printf("Case #%d: Volunteer cheated!\n", k+1);
		}else if(cont==1){
			printf("Case #%d: %d\n", k+1, last);
		}else{	
			printf("Case #%d: Bad magician!\n", k+1);
		}
	}
	return 0;
}