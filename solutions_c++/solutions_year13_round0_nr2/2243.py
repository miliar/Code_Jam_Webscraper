// prob2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

//#define out stdout

int numCases,n,m ;
int table[100][100];

bool process() {
	for(int h=1;h<=100;h++) {
		bool row[100],column[100];
		for(int i=0;i<n;i++) {
			row[i] = true ; 
			for(int j=0;j<m;j++) {
				if (table[i][j]>h) { row[i] = false ; break; }
			}
		}

		for(int j=0;j<m;j++) {
			column[j] = true ; 
			for(int i=0;i<n;i++) {
				if (table[i][j]>h) { column[j] = false ; break; }
			}
		}

		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if (table[i][j]==h && !row[i] && !column[j] ) {
					return false ; 
				}
			}
		}
	}

	return true ; 
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *in = fopen("B-large.in","r");
	FILE *out = fopen("output.txt","w");

	fscanf(in,"%d",&numCases);

	for(int cnt=0;cnt<numCases;cnt++) {
		fscanf(in,"%d %d",&n,&m);

		fprintf(out,"Case #%d:",cnt+1);

		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				fscanf(in,"%d",&table[i][j]);
			}
		}

		if (process()) {fprintf(out," YES\n"); } else { fprintf(out," NO\n"); }
	}

	fclose(in);
	fclose(out);
	
	return 0;
}

