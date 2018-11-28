//============================================================================
// Name        : Lawnmower.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void printMatrix(int *A, int N, int M){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cout << A[i*M + j];
		}
		cout << endl;
	}
}

bool checkColumn(int *A, int col, int N, int M){
	//all rows should be either one or two to not violate
	bool res;
	int sum = 0;
	for(int i = 0; i < N; i++){
		sum += A[i*M + col];
	}
	//check if all rows are ones or twos
	if((sum == N) or (sum == 2*N)){
		res = true;
	}else{
		res = false;
	}

	return res;
}

bool checkRow(int *A, int row, int N, int M){
	//all columns should be either one or two to not violate
	bool res;
	int sum = 0;
	for(int j = 0; j < M; j++){
		sum += A[row*M + j];
	}
	//check if all columns are ones or twos
	if((sum == M) or (sum == 2*M)){
		res = true;
	}else{
		res = false;
	}

	return res;
}

int main() {
	bool DEBUG = false;
	int cases;
	cin >> cases;
	for(int cnt = 1; cnt <= cases; cnt++){
		//read cases by case
		int N, M;
		cin >> N;
		cin >> M;
		int A[N*M];

		//read matrix row by row from stdin
		for(int j = 0; j < N; j++){
			for(int k = 0; k < M; k++){
				cin >> A[j*M + k];
			}
		}

		if(DEBUG){
			cout << "Case #" << cnt << ": " << "N=" << N << " M=" << M << endl;
			printMatrix(A, N, M);
		}

		bool rowViolates[N];
		bool colViolates[M];

		//check all columns to see if anyone violates
		for(int j = 0; j < M; j++){
			//first check if there is one in this column
			if(checkColumn(A, j, N, M) == false){
				if(DEBUG){
					cout << "column " << j << " violates!!!" << endl;
				}
				colViolates[j] = true;
			}else{
				colViolates[j] = false;
			}
		}

		//check all rows to see if anyone violates
		for(int i = 0; i < N; i++){
			//first check if there is one in this column
			if(checkRow(A, i, N, M) == false){
				if(DEBUG){
					cout << "row " << i << " violates!!!" << endl;
				}
				rowViolates[i] = true;
			}else{
				rowViolates[i] = false;
			}
		}

		//now check all squares
		bool possible = true;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				if((A[i*M + j] == 1) && rowViolates[i] && colViolates[j]){
					if(DEBUG){
						cout << "Violation happens in row " << i << " column " << j << endl;
					}
					possible = false;
					break;
				}
			}
			if(possible == false){
				break;
			}
		}

		if(possible){
			cout << "Case #" << cnt << ": " << "YES" << endl;
		}else{
			cout << "Case #" << cnt << ": " << "NO" << endl;
		}
		if(DEBUG){
			cout << "------------------------------------" << endl;
		}
	}

	return 0;
}
