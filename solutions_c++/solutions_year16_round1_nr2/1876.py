#include <iostream>
#include <cstdlib>
#include <list>
#include <cstring>

using namespace std;

/*
Vamos escolher um índice, i
Vamos pegar, de cada linha dada, o número que representa seu elemento i
Vamos contar quantas vezes esse elemento aparece como elemento i de todas as linhas
	Se for 2, nada pode ser declarado
	se for 1, então esse elemento está presente na linha que falta.
		Podemos pegar todos esses elementos que dão resultado 1, ordená-los, e teremos a linha final, resultante.
*/

//Will count how many times 'num' appears at all lines given.
int heights[2501];
void countHeights(int **array, int size, int innersize){	//Complexity O(size*innersize) = O(N*Ni)
	int i, j;
	
	memset(heights, 0, sizeof(heights));
	for(i = 0; i < size; i++)
		for(j = 0; j < innersize; j++)
			heights[array[i][j]]++;
}

int main(int argc, char *argv[]){
	int repeat, repti, N, Ni, i, j, hei;
	int **array;
	list<int> missingLine;

	cin >> repeat;
	for(repti = 0; repti < repeat; repti++){
		missingLine.clear();
		
		cin >> N;
		Ni = 2*N - 1;
		array = (int **) malloc(sizeof(int *) * Ni);		//Ni linhas
		for(i = 0; i < Ni; i++){
			array[i] = (int *) malloc(sizeof(int) * N);	//N elementos
			for(j = 0; j < N; j++){
				cin >> array[i][j];
			}
		}
	
		countHeights(array, Ni, N);
		for(i = 0; i < Ni; i++){
			for(j = 0; j < N; j++){
				//cout << "Counting " << array[i][j] << " returned " << K << endl;
				hei = array[i][j];
				if(heights[hei] % 2 == 1) missingLine.push_back(hei);
			}
		}
		missingLine.sort();
		missingLine.unique();
		missingLine.reverse();
		
		cout << "Case #" << repti+1 << ": ";
		for(i = 0; i < N; i++){
			cout << missingLine.back() << " ";
			missingLine.pop_back();
		}
		cout << endl;
		
		for(i = 0; i < Ni; i++)
			free(array[i]);
		free(array);
	}

	return 0;
}
