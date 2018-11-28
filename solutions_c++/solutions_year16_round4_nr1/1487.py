#include <bits/stdc++.h>
using namespace std;


int main(){
	int t;
	scanf(" %d", &t);
	for(int k = 1; k <= t; k++){
		int n, r, p, s;
		scanf(" %d %d %d %d", &n, &r, &p, &s);
		int flag = -1;
		
		int sol[2][10000];
		int size = pow(2, n);
		
		for(int i = 0; i < 3; i++){
			sol[0][0] = i;
			for(int j = 0; j < n; j++){
				int csize = pow(2, j);
				for(int l = 0; l < csize; l++){
					if(sol[j%2][l] == 0){
						sol[(j+1)%2][l*2] = 0;
						sol[(j+1)%2][l*2+1] = 2;
					} else if(sol[j%2][l] == 1){
						sol[(j+1)%2][l*2] = 1;
						sol[(j+1)%2][l*2+1] = 0;
					} else if(sol[j%2][l] == 2){
						sol[(j+1)%2][l*2] = 1;
						sol[(j+1)%2][l*2+1] = 2;
					}
				}
			}
			int nr = 0, np=0, ns=0;
			for(int j = 0; j < size; j++){
				if(sol[n%2][j] == 0){
					np++;
				} else if(sol[n%2][j] == 1){
					ns++;
				} else if(sol[n%2][j] == 2){
					nr++;
				}
			}
			if(np == p && ns == s && nr == r){
				flag = i;
				break;
			}
		}
		if(flag == -1){
			printf("Case #%d: IMPOSSIBLE\n", k);
		} else {
			for(int i = 0; i < size/2; i++){
				if(sol[n%2][i*2] == 1 && sol[n%2][i*2+1] == 2){
					sol[n%2][i*2] = 2;
					sol[n%2][i*2+1] = 1;
				}
				if(sol[n%2][i*2] == 1 && sol[n%2][i*2+1] == 0){
					sol[n%2][i*2] = 0;
					sol[n%2][i*2+1] = 1;
				}
			}
			for(int i = 0; i < size/4; i++){
				if(sol[n%2][i*4+1] == 1 && sol[n%2][i*4+3] == 2){
					sol[n%2][i*4+1] = 2;
					sol[n%2][i*4+3] = 1;
				}
			}
			printf("Case #%d: ", k);
			for(int i = 0; i < size; i++){
				if(sol[n%2][i] == 0){
					printf("P");
				} else if(sol[n%2][i] == 1){
					printf("S");
				} else {
					printf("R");
				}
			}
			printf("\n");
		}
	}
	return 0;
}
					