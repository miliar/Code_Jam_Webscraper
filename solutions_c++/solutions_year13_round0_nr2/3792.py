#include<stdio.h>
FILE *in=fopen("test.in","r");
FILE *out=fopen("test.out","w");

int main(){
	int T;
	int n,m;


	int left[110][110];
	int right[110][110];
	int up[110][110];
	int down[110][110];
	int d[110][110];

	int max;
	fscanf(in, "%d", &T);



	for(int k=1;k<=T;k++){
		fscanf(in, "%d %d", &n, &m );
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				fscanf(in, "%d", &d[i][j]);
				left[i][j]=right[i][j]=up[i][j]=down[i][j]=0;
			}
		}
		for(int i=1;i<=n;i++){
			max = 0;
			for(int j=1;j<=m;j++){
				if(max < d[i][j]) max = d[i][j];	
				left[i][j] = max;
			}
			max = 0 ;
			for(int j=m;j>=1;j--){
				if(max < d[i][j]) max = d[i][j];
				right[i][j]=max;
			}
		}

		for(int j=1;j<=m;j++){
			max = 0;
			for(int i=1;i<=n;i++){
				if(max < d[i][j]) max = d[i][j];
				up[i][j] = max;
			}
			max = 0;
			for(int i=n;i>=1;i--){
				if(max < d[i][j]) max = d[i][j];
				down[i][j]=max;
			}
		}


		bool isMake = false;;
		bool isAnswer = true;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				isMake = false;
				if(!(left[i][j] > d[i][j] || right[i][j] > d[i][j])) isMake = true;
				if(!(up[i][j] > d[i][j] || down[i][j] > d[i][j])) isMake = true;
				if(isMake == false) isAnswer = false;
			}
		}
		if(isAnswer == false) fprintf(out, "Case #%d: NO\n", k);
		else fprintf(out, "Case #%d: YES\n", k);
	}

}