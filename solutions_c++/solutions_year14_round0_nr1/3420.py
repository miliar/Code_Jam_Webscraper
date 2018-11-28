#include <stdio.h>
#include <iostream>

#define getchar_custom _fgetc_nolock
#define EOF_CHAR (-49)

inline int read_custom() {

    register int tempReadingChar = getchar_custom(stdin) - 48;

    while (tempReadingChar < 0 || tempReadingChar > 9) {
		if (tempReadingChar == EOF_CHAR) {
			return -1;
		}

        tempReadingChar = getchar_custom(stdin) - 48;
    }   

    register int returnValue = 0;

    while (tempReadingChar >= 0 && tempReadingChar <= 9) {
        returnValue = (returnValue << 3) + (returnValue << 1) + tempReadingChar;
        tempReadingChar = getchar_custom(stdin) - 48;
    }

    return returnValue;
}

void get_volunteer_answer(int* arr, int const& row) {

	int currentRow = 1;
	while (currentRow != row) {
		// skip not needed rows
		read_custom(); read_custom(); read_custom(); read_custom();
		currentRow++;
	}

	for (int j = 0; j < 4; j++) {
		*(arr + j) = read_custom();
	}
		
	int rowsLeft = 4 - row;
	for (int j = 0; j < rowsLeft; j++) {
		// skip not needed rows
		read_custom(); read_custom(); read_custom(); read_custom();
	}
}

void get_volunteer_answer_with_intersection(int const& row, int const* first_answer, int* output_array, int * output_length) {

	int o_length = 0;

	int currentRow = 1;
	while (currentRow != row) {
		// skip not needed rows
		read_custom(); read_custom(); read_custom(); read_custom();
		currentRow++;
	}

	register int readNo;
	for (int j = 0; j < 4; j++) {
		readNo = read_custom();
		for (int f = 0; f < 4; f++) {
			if (readNo == *(first_answer + f)) {
				*(output_array + o_length) = readNo;
				o_length++;
				break;
			}
		}
	}
		
	int rowsLeft = 4 - row;
	for (int j = 0; j < rowsLeft; j++) {
		// skip not needed rows
		read_custom(); read_custom(); read_custom(); read_custom();
	}

	*output_length = o_length;
}

int main() {
	
	int caseNo = read_custom();

	int* firstNo = new int[4];
	int* intersection_arr = new int[4];
	int intersection_length = 0;

	for (int i = 1; i <= caseNo; i++) {
		// FIRST TRY
		int volunteerAnswer = read_custom();
		get_volunteer_answer(firstNo, volunteerAnswer);

		// SECOND TRY
		volunteerAnswer = read_custom();		
		get_volunteer_answer_with_intersection(volunteerAnswer, firstNo, intersection_arr, &intersection_length);

		if (intersection_length == 0) {
			std::cout << "Case #" << i << ": Volunteer cheated!" << std::endl;
			continue;
		}

		if (intersection_length > 1) {
			std::cout << "Case #" << i << ": Bad magician!" << std::endl;
			continue;
		}

		std::cout << "Case #" << i << ": " << intersection_arr[0] << std::endl;
	}

	delete firstNo;
	delete intersection_arr;
}