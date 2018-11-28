#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	
	int n;
	
	scanf("%d",&n);
	
	for(int k=1;k <= n;k++){
		int c;
		int mat[4][4];
		int vet[20] = {0};
		
		scanf("%d", &c);
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&mat[i][j]);
				
				if(i == c-1){
					vet[mat[i][j]]+=1;
				}
			}
		}
		
		scanf("%d", &c);
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&mat[i][j]);
				
				if(i == c-1){
					vet[mat[i][j]]+=1;
				}
			}
		}
	
		int sum = 0;
		for(int i=1; i < 17 ;i++){
			if(vet[i] > 1){
				sum++;
			}
		}
		
		printf("Case #%d: ",k);
		if(sum == 0){
			printf("Volunteer cheated!\n");
		}else if(sum > 1){
			printf("Bad magician!\n");
		}else{
			for(int i = 1; i < 17;i++){
				if(vet[i] == 2){
					printf("%d\n",i);
					break;
				}
			}
		}
	}

	return 0;
}
