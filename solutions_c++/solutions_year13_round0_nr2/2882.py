#define maxar 124800
#define maxver 5000
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include<stdlib.h>
#include<map>

using namespace std;

int resp(int n, int m);


int matriz[110][110];
int maiorcol[110];
int maiorlin[110];


int main () {
	int casos =0, n, m;
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
	  scanf("%d %d",&n,&m);
	  for(int i=0;i<m;i++)maiorcol[i]=0;
	  for(int i=0;i<n;i++)maiorlin[i]=0;
	  
	  for(int i=0;i<n;i++){
	    for(int j=0;j<m;j++){
	      scanf("%d", &matriz[i][j]);
	      if(maiorcol[j]<matriz[i][j])maiorcol[j]=matriz[i][j];
	      if(maiorlin[i]<matriz[i][j])maiorlin[i]=matriz[i][j];
	    }
	  }
	  if(resp(n,m)==1)printf("Case #%d: YES", caso);
	  else printf("Case #%d: NO", caso);
	  printf("\n");

	}
return 0;
}

int resp(int n, int m){
  int i,j;
  for(i=0;i<n;i++){
    for(j=0;j<m;j++){
      if(matriz[i][j]!=maiorcol[j]&&matriz[i][j]!=maiorlin[i])return 0;
    }
  }

  return 1;
}

int max(int x, int y){
  if(x>y)return x;
  else return y;
}

		
	
	
	
	

	
