#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS


int isFull(int* num) {
	for (int i = 0; i < 10; i++) {
		if (*(num+i) == 0) return 0;
	}
	return 1;
}

int getSize(int num) {
	if (num < 10) {
		return 1;
	}
	int i = 1; 
	int num_len = 0;
	while (num >= i)
	{
		i *= 10;
		num_len++;
	}
	return num_len;
}

int* getDigit(int num, int size) {
	int* _num; int _size = size;
	_num = (int*)malloc(sizeof(int)*size);
	int i=1,j=0;

	if (size == 1) {
		*(_num) = num;
		return _num;
	}
	else {
		while ((size-1)) {
			i *= 10;
			size--;
		}

		while (_size) {
			if (num < 0) break;
			*(_num + j) = num / i;
			num %= i;
			i /= 10;
			j++;
			_size--;
		}
		return _num;
	}
}


int whenAsleep(int num) {
	int result = 0, size = 0;
	int temp;
	int* _num;
	int _check[10] = { 0,0,0,0,0,0,0,0,0,0 };
	for (int i = 1; i < 100; i++) {
		temp = num * i;
		size = getSize(temp);
		_num = getDigit(temp, size);
		for (int j = 0; j < size; j++) {
			if (*(_num + j) == 0) _check[0] ++;
			else _check[*(_num + j)]++;
		}
		free(_num);
		if (isFull(_check))
		{
			return temp;
		}
	}
	return result;
}

char* returnResult(int num, int i) {

	int result;
	
	char* resultString = (char*)malloc(sizeof(char) * 100);;
	result = whenAsleep(num);
	if (!result) {
		sprintf_s(resultString,100,"Case #%d: INSOMNIA", i);
		printf("%s\n", resultString);
	}
	else {
		sprintf_s(resultString,100,"Case #%d: %d", i, result);
		printf("%s\n", resultString);
	}
	

	return resultString;
}


int main() {

	FILE *input;
	FILE * output;
	int caseSize;
	int* num;
	int i = 0;
	input = fopen("A-large.in", "r");
	output = fopen("output.out", "w");
	fscanf(input, "%d", &caseSize);
	num = (int*)malloc(sizeof(int)*caseSize);
	for (i = 0; i < caseSize; i++) {
		fscanf(input, "%d\n", num + i);
		fprintf(output, "%s\n",returnResult(*(num + i), i+1));
	}
	fclose(input);
	fclose(output);
	getchar();
	return 0;
}