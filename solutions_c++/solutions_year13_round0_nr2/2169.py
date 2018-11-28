//============================================================================
// Name        : 130414-lawnmower.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>

int tab[105][105];
int col[105],row[105];

int main(){

	int m,n,st,test,i,j,k;

	scanf("%d",&test);

	for(k=1;k<=test;k++){

		st = 1;
		scanf("%d %d",&m,&n);

		for(i=0;i<m;i++) row[i] = 0;
		for(i=0;i<n;i++) col[i] = 0;

		for(i=0;i<m;i++)
			for(j=0;j<n;j++) scanf("%d",&tab[i][j]);

		//check
		for(i=0;i<m;i++)
			for(j=0;j<n;j++){
				if(tab[i][j]>row[i]) row[i] = tab[i][j];
				if(tab[i][j]>col[j]) col[j] = tab[i][j];
			}

		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				if(tab[i][j]!=row[i] && tab[i][j]!=col[j]) st = 0;

		if(st==1) printf("Case #%d: YES\n",k);
		else printf("Case #%d: NO\n",k);

	}

	return 0;
}
