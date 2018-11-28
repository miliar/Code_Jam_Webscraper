#include <cstring>
#include <cstdlib>
#include <cstdio>

int T;
int answer1,answer2;
int grid1[4][4];
int grid2[4][4];
int answers[16];
int main() {
	FILE* rfile = fopen("A-small.in" , "r");
	FILE* wfile = fopen("A-small.out", "w");
	fscanf(rfile,"%d",&T);
	for(int cases=0;cases<T;cases++) {
		memset(answers,0,sizeof(answers));
		fscanf(rfile,"%d",&answer1);
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				fscanf(rfile,"%d",&grid1[i][j]);
			}
		}
		fscanf(rfile,"%d",&answer2);
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				fscanf(rfile,"%d",&grid2[i][j]);
			}
		}
		for(int i=0;i<4;i++) {
			answers[grid1[answer1-1][i]-1]++;
			answers[grid2[answer2-1][i]-1]++;
		}
		bool twotwo = false;
		int answer=-1;
		for(int i=0;i<16;i++) {
			if(answers[i]==2) {
				if(answer!=-1)twotwo = true;
				else answer = i+1;
			}
		}
		if(answer==-1)fprintf(wfile,"Case #%d: Volunteer cheated!\n",cases+1);
		else if(twotwo)fprintf(wfile,"Case #%d: Bad Magician!\n",cases+1);
		else fprintf(wfile,"Case #%d: %d\n",cases+1,answer);
	}



	fclose(rfile);
	fclose(wfile);
}