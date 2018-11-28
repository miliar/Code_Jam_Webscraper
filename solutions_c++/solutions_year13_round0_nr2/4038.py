#include<iostream>
#include<sstream>
#include<cstdio>
#include<stack>
#include<queue>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#define MAX 120
using namespace std;

bool presentNumbers[MAX];

template <size_t size_y>
bool checkHorizontal(int arr[][size_y], int numRow, int maxColumn){
	//bool horizontalDifferent = false;
	for (int J = 0;  J< maxColumn - 1; J++){
	if (arr[numRow][J] != arr[numRow][J + 1]){
		return false;
	}
}
	return true;
}

template <size_t size_y>
bool checkVertical(int arr[][size_y], int maxRow , int numColumn){
for (int I = 0; I< maxRow - 1; I++){
	if (arr[I][numColumn] != arr[I + 1][numColumn]){
		return false;
	}
}
	return true;
}
template<size_t size_y>
int findBiggest(int arr[][size_y], int row, int column){
int max = 0;
for (int I = 0; I < row; I++){
	for (int J = 0; J < column; J++){
		if (arr[I][J]>max){
			max = arr[I][J];
		}
	}
}
return max;
}

template<size_t size_y>
int findBiggestRow(int arr[][size_y], int row, int column){
int max = 0;

for (int J = 0; J < column; J++){
		if (arr[row][J]>max){
			max = arr[row][J];
		}
}
return max;
}

template <size_t size_y>
int findBiggestColumn(int arr[][size_y], int row, int column){
int max = 0;
for (int I = 0; I < row; I++){
		if (arr[I][column]>max){
			max = arr[I][column];
		}
	}
return max;
}


int main(){
freopen("input.in", "r", stdin);
freopen("output.out", "w", stdout);
int T;
int row;
int column;
int numCases = 0;
int arreglo[MAX][MAX];
int arregloPrimo[MAX][MAX];
int I;
int J;
int K;
int L;
int M;
bool areDifferent = false;
int upperHorizontal = 0;
int lowerHorizontal = 0;
int leftColumn = 0;
int rightColumn = 0;
int biggest = 0;
scanf("%d", &T);

while (numCases<T){
//areDifferent = false;
scanf("%d%d", &row, &column);

// initializePresentNumbers

for (I = 0; I < MAX; I++){
	presentNumbers[I]=false;
}

for (I = 0; I < row; I++){
	for (J = 0; J < column; J++){
		scanf("%d", &arreglo[I][J]);
		if(presentNumbers[arreglo[I][J]]!=true){
			presentNumbers[arreglo[I][J]]=true;
		}
	}
}

for (K = 100; K >= 1; K--){
	if (presentNumbers[K]){
		for (I = 0; I < row; I++){
			for (J = 0; J < column; J++){
				if (arreglo[I][J]==K){

					if (findBiggestRow(arreglo,I, column)== K){
						for (L = 0; L< column; L++){
							arregloPrimo[I][L] = K;
						}
					}
					if (findBiggestColumn(arreglo, row, J) == K){
							for (M = 0; M < row; M++){
							arregloPrimo[M][J] = K;
						}
					}
				}
			}	
		}
	}
}
/*biggest=findBiggest(arreglo, row, column);
for (I = 0; I < row; I++){
	for (J = 0; J < column; J++){
		arregloPrimo[I][J] = biggest;
	}
}

for (I = 0; I < row; I++){
if (checkHorizontal(arreglo, I, column)){
	for (J = 0; J< column; J++){
	arregloPrimo[I][J] = arreglo[I][J];
}
}
}

for (J = 0; J < column; J++){
if (checkVertical(arreglo, row , J)){
	for (I = 0; I < row; I++){
	arregloPrimo[I][J] = arreglo[I][J];
}
}
}
*/
for (I = 0; I < row; I++){
	for (J = 0; J < column; J++){
		if (arregloPrimo[I][J] != arreglo[I][J]){
			areDifferent = true;
			break;
		}
	}
	if (areDifferent){
		break;
	}
}

/*printf("\nArreglo\n");
for (I = 0; I < row; I++){
	for (J = 0; J < column; J++){
		printf("%d", arreglo[I][J]);
	}
	printf("\n");
}
printf("\nArreglo Primo\n");

for (I = 0; I < row; I++){
	for (J = 0; J < column; J++){
		printf("%d", arregloPrimo[I][J]);
	}
	printf("\n");
}
printf("\n");*/

numCases++;
printf("Case #%d: ", numCases);

if (!areDifferent){
	printf("YES\n");
}
else{
	printf("NO\n");
}
areDifferent = false;
}
return 0;
}

