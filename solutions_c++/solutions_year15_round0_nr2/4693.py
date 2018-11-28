#include <stdlib.h>
#include <stdio.h>

int max(int*, int);
int check(int, int, int*, int);

int main(){
	//freopen("input.in","r",stdin);
	//freopen("output.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	int T, D, *Pi;
	int biggest_plate = 0;
	int moves;

	scanf("%d", &T);

	for(int x = 0; x < T; ++x){
	
		scanf("%d", &D);
		Pi = new int[D];
		for(int y = 0; y < D; ++y){
			scanf("%d", &(Pi[y]));
		}

		biggest_plate = max(Pi, D);
		moves = biggest_plate;
		while(biggest_plate >= 2){
			moves = check(biggest_plate, moves, Pi, D);
			--biggest_plate;
		}
		printf("Case #%d: %d\n", x + 1, moves);
	}


	return 0;
}

int max(int* array, int length){

	int m = array[0];
	for(int x = 1; x < length; ++x){
		if(m < array[x]){
			m = array[x];
		}
	}
	return m;
}

int check(int height, int moves, int* Pi, int length){

	int aux = height;
	for(int x = 0; x < length; ++x){
		aux += (Pi[x] - 1) / height;
		if(moves < aux){
			return moves;
		}
	}

	return aux;
}

