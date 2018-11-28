#include<stdio.h>


int T, N,M, Tcount;
int map[101][101];
int check[101][101];
FILE *fp, *fout;
int flag = 0;

void input();
void process();
void output();

int main(){
	fp = fopen("input.txt","r");
	fout = fopen("output.txt", "w");
	fscanf(fp,"%d", &T);
	for(Tcount = 1; Tcount <= T; Tcount++){
		input();
		process();
		output();
	}
	return 0;
}

void input(){
	int i,j;
	fscanf(fp,"%d%d", &N,&M);
	for(i=1;i<=N;i++)
		for(j=1;j<=M;j++) check[i][j] = 0;
	for(i=1;i<=N;i++){
		for(j=1;j<=M;j++){
			fscanf(fp,"%d",&map[i][j]);

		}
	}
}

void process(){
	int i, j, k, count;
	flag= 0;
	for(k = 1;k <=99;k++){
		for(i=1;i<=N;i++){
			count = 0;
			for(j=1;j<=M;j++){
				if(map[i][j] == k) count++;
			}
			if(count == M){
				for(j=1;j<=M;j++){
					check[i][j] = 1;
				}
			}
		}
		for(i=1;i<=M;i++){
			count = 0;
			for(j=1;j<=N;j++){
				if(map[j][i] == k) count++;
			}
			if(count == N){
				for(j=1;j<=N;j++){
					check[j][i]=1;
				}
			}
		}
		for(i=1;i<=N;i++){
			for(j=1;j<=M;j++){
				if(check[i][j] == 1){
					check[i][j] = 0;
					map[i][j]++;
				}
			}
			//if(flag==1) break;
		}

		for(i=1;i<=N;i++){
			for(j=1;j<=M;j++){
				if(map[i][j] == k){
					flag = 1;
					break;
				}
			}
		}
		//if(flag == 1) break;
	}
}

void output(){
	fprintf(fout,"Case #%d: ",Tcount);
	if(flag == 0) fprintf(fout,"YES\n");
	else fprintf(fout, "NO\n");
}