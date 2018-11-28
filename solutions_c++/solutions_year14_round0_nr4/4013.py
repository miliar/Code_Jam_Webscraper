#include <stdio.h>
#include <iostream>

void insertionSortD(double array[], int tamanho) {
      int i, j;
	  double tmp;
      for (i = 1; i < tamanho; i++) {
            j = i;
            while (j > 0 && array[j - 1] < array[j]) {
                  tmp = array[j];
                  array[j] = array[j - 1];
                  array[j - 1] = tmp;
                  j--;
            }
      }
}
void insertionSortC(double array[], int tamanho) {
      int i, j;
	  double tmp;
      for (i = 1; i < tamanho; i++) {
            j = i;
            while (j > 0 && array[j - 1] > array[j]) {
                  tmp = array[j];
                  array[j] = array[j - 1];
                  array[j - 1] = tmp;
                  j--;
            }
      }
}

void dw(FILE *p,int t,FILE *q){
	int n,i,j,score1=0,score2=0;
	int cont=0; //cont to get last min from ken's weight
	//double *ptr; //aux to burn Ken's min weight game1 and 2
	fscanf(p,"%d",&n);
	double *cn = new double[n]; //naomi's weights
	double *ck = new double[n]; //ken's weights
	double *auxk = new double[n]; //aux to ken's weight
	double *auxn = new double[n]; //aux to naomi's weight

	for (i=0;i<n;i++){
		fscanf(p,"%lf",&cn[i]);
	}
	for (i=0;i<n;i++){
		fscanf(p,"%lf",&ck[i]);
	}
	insertionSortC(cn,n);
	insertionSortC(ck,n);
	
	for(i=0;i<n;i++){
		*(auxn+i)=*(cn+i);
		*(auxk+i)=*(ck+i);
	}
	double a,b;
	//Deceitful War optimally (score2)
	for(i=0;i<n;i++){
		a=auxn[i];
		b=auxk[i];
		if(auxn[i]<auxk[i]){
			//ck[i]=-1;
			auxk[n-1]=-1;
			insertionSortC(auxk,n);
		}
	}
	for(i=0;i<n;i++){
		if(auxk[i]!=-1){
			score2++;
		}
	}
	//ptr = &ck[0];
	//Optimally War game (Score1)
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			//score2
			//&& ck[j] != -1
			//score1
			if(cn[i] < ck[j]){
				ck[j]=-1;
				insertionSortC(ck,n);
				cont++;
				score1++;
				break;
			}
			if(j==n-1 && ck[j] < cn[i]){
				ck[cont]=-1;
			}
		}
	}
	score1=n-score1;

	printf("Case #%d: %d %d\n\n",t,score2,score1);
	fprintf(q,"Case #%d: %d %d\n",t,score2,score1);
	//ptr = NULL;
	auxn=NULL;
	auxk=NULL;
	//delete ptr;
	delete[] cn;
	delete[] ck;
	delete[] auxn;
	delete[] auxk;
}

int main(){
	char c;
	int t,n=1;
	FILE *p,*q;
	q = fopen("output.txt","w");
	if (q==NULL){ 
		printf( "erro\n\n");
	}
	p = fopen("D-large.in","r");
	if (p==NULL){ 
	printf( "erro\n\n");
	}
	fscanf(p,"%d",&t);
	//printf("%d\n",t);

	while (!feof(p)){
		dw(p,n,q);
		n++;
	}
	system("PAUSE");
	return 0;
}
/*
*/