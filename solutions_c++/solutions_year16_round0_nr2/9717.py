#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

bool *getPancakes(int *size){
	int i;
	bool *array;
	string input;
	cin >> input;
	*size = input.size();
	array = (bool *) malloc(sizeof(int) * (*size));
	for(i = 0; i < *size; i++){
		if(input[i] == '+') array[i] = true;
		else array[i] = false;
	}
	return array;
}

// + + + + + + - - - + + + - - - +
//                     |
// 0 1 2 3 4 5 6 7 8 9 10
void flipPancakes(bool *array, int pos){	//Flip every pancake from position pos all the way to the highest pancake aka array[size - 1]
	int i, aux, lim;
	
	lim = (pos)/2;
	for(i = 0; i <= lim; i++){
		aux = !array[i];
		array[i] = !array[pos-i];
		array[pos-i] = aux;
	}
}

void printPancakes(bool *array, int size){	//For debugging.
	int i;
	for(i = 0; i < size; i++)
		if(array[i] == true) cout << "+";
		else cout << "-";
	cout << endl;
}

int deliverPancakes(){
	int i, j, size, counter = 0;
	bool *array;
	array = getPancakes(&size);
	//printPancakes(array, size);
	for(i = size - 1; i >= 0; i--){
		if(array[i] == false){
			if(array[0] == false){
				//cout << "Flipping" << endl;
				flipPancakes(array, i);
				//printPancakes(array, size);
				counter++;
			}else{
				for(j = 0; array[j] == true; j++);
				//cout << "Flipping twice" << endl;
				flipPancakes(array, j-1);
				//printPancakes(array, size);
				counter++;
				flipPancakes(array, i);
				//printPancakes(array, size);
				counter++;
			}
		}
		//cout << "..." << endl;
	}
	free(array);
	return counter;
}

int main(int argc, char *argv[]){
	int ncases, n;
	int i, result;
	
	cin >> ncases;
	for(i = 1; i <= ncases; i++){
		result = deliverPancakes();
		cout << "Case #" << i << ": " << result << endl;
	}
	
	return 0;
}
