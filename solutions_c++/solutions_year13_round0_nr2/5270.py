#include <string>
#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
	
	int T, Total,N,M,i,j;
	int max_r;
	int max_c;
	int* maxrows;
	int* maxcols;
	cin>>T;
	Total = T;
	int** lawn;
	while(T--){
		cin>>N>>M;
		lawn = new int*[N];
		maxrows = new int[N];
		maxcols = new int[M];
		for(i=0;i<N;i++){
			max_r = 0;
			lawn[i] = new int[M];
			for(j=0;j<M;j++){
				cin>>lawn[i][j];
				max_r = max(max_r,lawn[i][j]);
			}
			maxrows[i] = max_r;
		}
		for(i=0;i<M;i++){
			max_c = 0;
			for(j=0;j<N;j++){
				max_c = max(max_c,lawn[j][i]);
			}
			maxcols[i] = max_c;
		}

		bool flag = true;
		for(i=0;i<N && flag;i++){
			for(j=0;j<M;j++){
				if(lawn[i][j] < min(maxrows[i],maxcols[j])){
					printf("Case #%d: %s\n",Total-T,"NO");
					flag = false;
					break;
				}
			}
		}
		if(flag == true){
			printf("Case #%d: %s\n",Total-T,"YES");
		}
		
		// free space
		for(i=0;i<N;i++){
			delete[] lawn[i];
		}

		delete[] lawn;
		delete[] maxrows;
		delete[] maxcols;
	}
	return 0;
}