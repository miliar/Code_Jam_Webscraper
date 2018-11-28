#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>

using namespace std;

int T, Smax;
int Saud[1111];
int cnt, nowstand, frie;

int main()
{
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin,"%d",&T);
	for(int t=1;t<=T;t++){
		cnt=0;
		nowstand=0;
		fscanf(fin,"%d",&Smax);
		for(int i=0;i<=Smax;i++){
			fscanf(fin,"%1d",&Saud[i]);
		}
		for(int i=0;i<=Smax;i++){
			if(nowstand>=i){
				nowstand+=Saud[i];
			}
			else{
				frie = i-nowstand;
				cnt+=frie;
				nowstand+=frie;
				nowstand+=Saud[i];
			}
		}
		fprintf(fout,"Case #%d: %d\n",t,cnt);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}