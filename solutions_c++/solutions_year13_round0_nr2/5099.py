#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void readTable(int M, int N, int **pTable)
{
	for(int i=0; i < M; ++i)
      for(int j=0; j<N; ++j) {
			scanf("%d", &pTable[i][j]);
      		//printf("%d", pTable[i][j]);
		}
}

bool canWeCutbyRow(int N, int row, int **pTable, int ht) {
	for(int i=0; i<N; ++i) 
		if(pTable[row][i] > ht)
			return false;
	
	return true;
}

bool canWeCutbyCol(int M, int col, int **pTable, int ht) {
	for(int i=0; i<M; ++i) 
		if(pTable[i][col] > ht)
			return false;
	
	return true;
}

void getRowHts(int N, int row, int **pTable, bool **pWTable, int &mxht, int &minht)
{
	mxht = 0;
	minht = 99;
	for(int i=0; i<N; ++i) {
		if(pWTable[row][i] == false) {
			if(pTable[row][i] > mxht) {
				mxht = pTable[row][i];
			}
			
			if(pTable[row][i] < minht) {
				minht = pTable[row][i];
			}
		}
	}
}

void getColHts(int M, int col, int **pTable, bool **pWTable, int &mxht, int &minht)
{
	mxht = 0;
	minht = 99;
	for(int i=0; i<M; ++i) {
		if(pWTable[i][col] == false) {
			if(pTable[i][col] > mxht) {
				mxht = pTable[i][col];
			}
			
			if(pTable[i][col] < minht) {
				minht = pTable[i][col];
			}
		}
	}
}

void cutGrassbyRow(int N, int row, int **pTable, bool **pWTable, int ht)
{
	for(int i=0; i<N; ++i) {
		if((pWTable[row][i] == false) && (pTable[row][i] == ht)) {
			pWTable[row][i] = true;
		}
	}
}

void cutGrassbyCol(int M, int col, int **pTable, bool **pWTable, int ht)
{
	for(int i=0; i<M; ++i) {
		if((pWTable[i][col] == false) && (pTable[i][col] == ht)){
			pWTable[i][col] = true;
		}
	}
}

bool getResult(int M, int N, bool **pWTable) 
{
	for(int i=0; i < M; ++i)
      for(int j=0; j<N; ++j) {
			if(pWTable[i][j] == false)
				return false;
		}
		
	return true;
}

int main()
{
	int T, M, N;
	int **pTable = 0;
	bool **pWTable = 0;//worker table
	
	scanf("%d", &T);
	for(int idx =1; idx <= T; idx++) {
		scanf("%d%d", &M, &N);
      	//printf("\n%d %d\n", M, N);
		pTable = (int**)malloc(M*sizeof(int*));
		pWTable = (bool**)malloc(M*sizeof(bool*));
		int *array = (int *)malloc(M*N*sizeof(int));
		bool *warray = (bool *)malloc(M*N*sizeof(bool));
		memset(warray, 0x00, M*N*sizeof(bool));
		
        for(int i=0; i < M; ++i) {
          pTable[i] = array + (N*i);
		  pWTable[i] = warray+ (N*i);		  
        }
		
		readTable(M, N, pTable);
		
		//cut grass by rows
		for(int i=0; i < M; ++i) {
				int mxht=0, minht=0;
				getRowHts(N, i, pTable, pWTable, mxht, minht);
				//printf("%d hts: %d %d\n", i, mxht, minht);
				if(mxht && minht) {
					while(mxht >= minht){
						if(!canWeCutbyRow(N, i, pTable, mxht)) 
							break;
						
						cutGrassbyRow(N, i, pTable, pWTable, mxht);
						--mxht;
					}
				}
			
		}
		
		//cut grass by cols
		for(int i=0; i < N; ++i) {
			int mxht=0, minht=0;
			getColHts(M, i, pTable, pWTable, mxht, minht);
			//printf("%d hts: %d %d\n", i, mxht, minht);
			if(mxht && minht) {
				while(mxht >= minht){
					if(!canWeCutbyCol(M, i, pTable, mxht)) 
						break;
								
					cutGrassbyCol(M, i, pTable, pWTable, mxht);
					--mxht;
				}
			}
		}
		
		//check if pattern possible and print result
		printf("Case #%d: %s\n", idx, getResult(M, N, pWTable) ? "YES" : "NO");
		
		free(array);
		free(warray);
        free(pTable);
		free(pWTable);
	}
}