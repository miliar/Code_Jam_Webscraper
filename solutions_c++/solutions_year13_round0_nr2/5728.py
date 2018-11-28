#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
	int cols[100];
	int rows[100];
	int map[100][100];
	int T;
	int n;
	int m;
	FILE * in = fopen("input.txt", "r");
	FILE * out = fopen("output.txt", "w");
	
	fscanf(in, "%d", &T);
	
	int num;
	
	for(int t=1;t<=T;t++){
		memset(cols, 0, sizeof(int)*100);
		memset(rows, 0, sizeof(int)*100);
		fscanf(in, "%d %d", &n, &m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				fscanf(in, "%d", &num);
				rows[i]=max(rows[i], num);
				cols[j]=max(cols[j], num);
				map[i][j]=num;
			}
		}
		bool possible = true;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(map[i][j]<min(rows[i], cols[j])) possible=false;
			}
		}
		if(possible) fprintf(out, "Case #%d: YES\n", t);
		else fprintf(out, "Case #%d: NO\n", t);
	}
	
	return 0;
}
