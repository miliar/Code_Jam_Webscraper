#include <stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

FILE *ptr;

void solve(int c){
	int map[100][100];
	int map2[100][100];
	int level = 100;
	int m,n;
	int max = 0;
	int temp;
	cin >> n >> m;
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin >> temp;
			if(temp > max) max = temp;
			map[i][j] = temp;
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			map2[i][j] = max;
		}
	}
	for(int k=max-1;k>0;k--){
		for(int i=0;i<n;i++){
			int boo = 1;
			for(int j=0;j<m;j++){
				if(map[i][j] > k){
					boo = 0;
				}
			}
			if(boo > 0){
				for(int j=0;j<m;j++){
					map2[i][j] = k;
				}
			}
		}
		for(int i=0;i<m;i++){
			int boo = 1;
			for(int j=0;j<n;j++){
				if(map[j][i] > k){
					boo = 0;
				}
			}
			if(boo > 0){
				for(int j=0;j<n;j++){
					map2[j][i] = k;
				}
			}
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(map[i][j] != map2[i][j]){
				//printf("Case #%d: NO\n",c);
				fprintf(ptr,"Case #%d: NO\n",c);
				return ;
			}
		}
	}
	//printf("Case #%d: YES\n",c);
	fprintf(ptr,"Case #%d: YES\n",c);
}

int main(){
	int n;
	cin >> n;
	ptr = fopen("bans.txt","w");
	for(int i=0;i<n;i++){
		solve(i+1);
	}
	fclose(ptr);
	return 0;
}