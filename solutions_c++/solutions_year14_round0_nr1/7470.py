#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>

#define REP(i,a,b) for(int i=a;i<=b;i++)
#define sf scanf
#define pf printf

using namespace std;

int a[5][5] , b[5][5];
int r1,r2;

FILE *fin = fopen("A-small-attempt1.in","r");
FILE *fout= fopen("data.out","w");

int main(){

	int t; fscanf(fin,"%d",&t);
	REP(it,1,t){
		fscanf(fin,"%d",&r1);
		REP(i,1,4) REP(j,1,4) fscanf(fin,"%d",&a[i][j]);
		fscanf(fin,"%d",&r2);
		REP(i,1,4) REP(j,1,4) fscanf(fin,"%d",&b[i][j]);
		
		int ans ,ansk=0;
		REP(i,1,4) REP(j,1,4) 
			if( a[r1][i]==b[r2][j] ){
				ans = a[r1][i]; ansk++;
			}
		fprintf(fout,"Case #%d: ",it);
		if( ansk>1 ) fprintf(fout,"Bad magician!\n");
		else if( ansk==0 ) fprintf(fout,"Volunteer cheated!\n");
		else fprintf(fout,"%d\n",ans);
	}

	return 0;
}