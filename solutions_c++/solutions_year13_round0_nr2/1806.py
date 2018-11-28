#include <stdio.h>
#define max(a,b) ((a>b)?a:b)

void initArr(int A[], int size){ for (int i = 0; i < size; ++i) A[i] = 0; }

int chkArr(int A[][100], int n, int m, int rowMax[], int colMax[]){
	for (int i = 0; i < n; ++i)	for (int j = 0; j < m; ++j)
		if(A[i][j] < rowMax[i] && A[i][j] < colMax[j]) return 0;
	return 1;
}

int main(){

	const char* pRes[]={"NO", "YES"}; char* result;
	int t,n,m,i,j;
	int A[100][100], rowMax[100]={}, colMax[100]={};
	scanf("%d", &t);
	for(int k = 1; k<=t; k++){
		scanf("%d%d",&n,&m);
		initArr(rowMax,n);
		initArr(colMax,m);
		for (i = 0; i < n; ++i){
			for (j = 0; j < m; ++j){
				scanf("%d",&A[i][j]);
				rowMax[i] = max(rowMax[i], A[i][j]);
				colMax[j] = max(colMax[j], A[i][j]);
			}
		}

		i = chkArr(A,n,m,rowMax,colMax);
		result = (char*)pRes[chkArr(A,n,m,rowMax,colMax)];
		printf("Case #%d: %s\n", k, result);
	}
	return 0;
}