#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>

using namespace std;

int T, X,R,C;
int ans;


int main()
{
	FILE *fin = fopen("D-small-attempt0.in", "r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin,"%d",&T);
	for(int t=1;t<=T;t++){
		fscanf(fin,"%d %d %d",&X,&R,&C);
		ans=0;
		if(X==1) ans=1;
		if(X==2){
			if((R*C)%X==0) ans=1;
		}
		if(X==3){
			if(R%3==0 && C>=2){
				ans=1;
			}
			else if(R>=2 && C%3==0){
				ans=1;
			}
		}
		if(X==4){
			if(R%4==0 && C>=3){
				ans=1;
			}
			if(R>=3 && C%4==0){
				ans=1;
			}
		}
		if(X==5){
			if(R%5==0 && C>=4){
				ans=1;
			}
			if(R>=4 && C%5==0){
				ans=1;
			}
		}
		if(X==6){
			if(R%6==0 && C>=5){
				ans=1;
			}
			if(R>=5 && C%6==0){
				ans=1;
			}
		}

		fprintf(fout,"Case #%d: ",t);
		if(ans==1) fprintf(fout,"GABRIEL\n");
		if(ans==0) fprintf(fout,"RICHARD\n");
	}

	fclose(fin);
	fclose(fout);

	return 0;
}