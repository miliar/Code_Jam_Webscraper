#include <stdio.h>

static int lawn[100][100];

bool isAllSame(int i,int m){
	int key = lawn[i][0];
	int j=0;
	for(j=1;j<m;j++){
		if(lawn[i][j] != key) return false;
	}
	return true;
}

bool isAllSameJ(int j,int n){
	int key = lawn[0][j];
	int i=1;
	for(i=1;i<n;i++){
		if(lawn[i][j] != key) return false;
	}
	return true;
}
int main(void){
	int t=0;
	int n,m;
	FILE* inp = fopen("inp.txt","r");
	FILE* out = fopen("out.txt","w");
	int numCase = 1;
	int i,j,temp;
	bool res;
	fscanf(inp,"%d",&t);
	for(numCase = 1;numCase<=t;numCase++){
		fscanf(inp,"%d",&n);
		fscanf(inp,"%d",&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				fscanf(inp,"%d",&temp);
				lawn[i][j] = temp;
			}
		}
		res = true;
		for(i=0;i<n;i++){
			if(!isAllSame(i,m)){
				for(j=0;j<m;j++){
					if(lawn[i][j] ==1){
						if(!isAllSameJ(j,n)){
							res = false;
							goto out;
						}
					}
				}
			}
		}
out:
		if(res)
			fprintf(out,"Case #%d: YES\n",numCase);
		else
			fprintf(out,"Case #%d: NO\n",numCase);

	}
}