#include <iostream>

using namespace std;


int main(){
	int T;
	cin>>T;
	int matA[4][4];
	int matB[4][4];

	for(int cc = 0;cc<T;++cc){
		int ra, rb;
		cin>>ra;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin>>matA[i][j];
			}
		}
		cin>>rb;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin>>matB[i][j];
			}
		}

		int sameCnt = 0;
		int same;
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k){
				if(matA[ra-1][j] == matB[rb-1][k]){
					++sameCnt;
					same = matA[ra-1][j];
				}
			}
		}

		printf("Case #%d: ", cc+1);
		if(sameCnt==0){
			printf("Volunteer cheated!\n");
		} else if(sameCnt==1){
			printf("%d\n", same);
		} else {
			printf("Bad magician!\n");
		}
	}
}