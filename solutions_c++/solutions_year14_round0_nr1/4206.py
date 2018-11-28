#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>

using namespace std;

#define SIZE 4

int i, j;

int** create_matrix (int matrix_size){
	int **matrix = new int* [matrix_size];
	
	for (i = 0; i < matrix_size; i++)
		matrix[i] = new int[matrix_size];

	return matrix;
}

/*********************************************/

void finding_the_card_row(int** matrix, int position, int* array){

	for (i = 0; i < SIZE; i++){
		array[i] = matrix[position][i];
	}
}

/****************************************************************/
/****************************************************************/

void finding_the_card(int* first_array, int* second_array){
	int temp, equal_card = 0, card_number;
	string result;

	for (i = 0; i < SIZE; i++){
		temp = first_array[i];

		for (j = 0; j < SIZE; j++){
			if (temp == second_array[j]){
				equal_card++;
				card_number = temp;
			}
		}
	}

	if (equal_card == 0)
		cout << "Volunteer cheated!" << endl;
	else if(equal_card == 1)
		cout << card_number << endl;
	else if (equal_card >= 2)
		cout << "Bad magician!" << endl;

}


/****************************************************************/
/****************************************************************/

void print_matrix (int **matrix, int matrix_size){
	for (i = 0; i < matrix_size; i++){
		for (j = 0; j < matrix_size; j++){
			cout << matrix[i][j];
		}
		if (i != matrix_size - 1)
			cout << endl;
	}
}

/****************************************************************/
/****************************************************************/

void populate_matrix (int **matrix, int matrix_size){
	for (i = 0; i < matrix_size; i++){
		for (j = 0; j < matrix_size; j++){
			cin >> matrix[i][j];
		}
	}
}

/****************************************************************/
/****************************************************************/


int main (){
	int **matrix;

	int *first_array = new int[SIZE];
	int *second_array = new int[SIZE];

	int testcases, card_row_position, count = 1; 

	cin >> testcases;

	matrix = create_matrix(SIZE);

	for (int index = 0; index < testcases; index++){

		for (int index2 = 0; index2 < 2; index2++){
			cin >> card_row_position;

			populate_matrix(matrix, SIZE);

			if (index2 == 0)
				finding_the_card_row(matrix, card_row_position - 1, first_array);
			else
				finding_the_card_row(matrix, card_row_position - 1, second_array);

			//cout << first_array[0] << " " << first_array[1] << " " << first_array[2] << " " << first_array [3] << endl;
			//cout << second_array[0] << " " << second_array[1] << " " << 
			//        second_array[2] << " " << second_array [3] << endl;

			//print_matrix (matrix, SIZE);
		}	

		cout << "Case #" << count << ": "; 
		finding_the_card(first_array, second_array);

		count++;

	}

	free (matrix);

	return 0;
}