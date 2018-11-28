#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>

#include <algorithm>
#include <math.h>
#include <vector>

#include <stdio.h>
using namespace std;

int** arr;
int N = 0;
int M = 0;

int maxElement(int *a, int size)
{
	//cout<<"array at max"<<endl;

	//for(int j = 0; j < size; j++)
	//{
	//	cout<<a[j];
	//}

	int mMax = a[0];
	for(int i = 0; i < size; i++) {
		if(a[i] > mMax)
			mMax = a[i];
	}
	return mMax;
}

int minElement(int *a, int size)
{
	//cout<<"array at max"<<endl;

	//for(int j = 0; j < size; j++)
	//{
	//	cout<<a[j];
	//}

	int mMax = a[0];
	for(int i = 0; i < size; i++) {
		if(a[i] > mMax)
			mMax = a[i];
	}
	return mMax;
}

int *getRow(int i)
{
	int *row = new int[M];
	for(int j = 0; j < M; j++)
	{
		row[j] = arr[i][j];
	}

	return row;
}

int *maxInRow()
{
	int *array = new int[N]; 
	for(int i = 0; i < N; i++){
		int * row = getRow(i);
		array[i] = maxElement(row, M);
	}

	return array;
	
}

int* getColumn(int j){
	int *column = new int[N];

	for(int i = 0; i < N; i++) {
		column[i] = arr[i][j];
	}

	return column;
}


int *maxInColumns()
{

	int *array = new int[M];
	for(int c = 0; c < M; c++){
			array[c] = maxElement(getColumn(c), N);
	}

	return array;
}



int check()
{
	int *rowsMax = maxInRow();
	int *colsMax = maxInColumns();
	
	//if(solve < 0) {
	//	return -1;	
	//}

	for( int i = 0; i < N; i++) {
		for (int j =0; j < M; j++) {
			if((arr[i][j] != rowsMax[i]) && (arr[i][j] != colsMax[j])) {			
				return -1; //fail
			}
		}
 	}

	

	//good
	return 0;
}

int getMinInRow(int i)
{
	int min = arr[i][0];
	int index = 0;
	for(int j = 0; j < M; j++)
	{
		if(arr[i][j] < min){
			min = arr[i][j];
			index = j;
		}
	}
	return min;
}

int checkRow(int i, int min) {
	int xCounter = 0;

	bool *row = new bool[M];
	for(int j = 0; j < M; j++) {
		row[j] = true;
	}

	bool indicator = true;
	for(int j = 0; j < M; j++) {
		if(arr[i][j] == min) {
			xCounter++;

			for(int k = 0; k < N; k++) {
				if(arr[k][j] != min) {
					row[j] = false;
					indicator = false;
				}
			}

		} 
	}

	if((xCounter != M-1)||(!indicator))
	{
		return -1;
	}

	return 0;
	//{
	//	for(int j = 0; j < M; j++) {
		//	if(row[j]
	//	}/
	//}
}

int solve()
{
	for(int i = 0; i < N; i++) {
		int min = getMinInRow(i);
		int result = checkRow(i, min);
		
		if(result < 0) 
			return result;	
	}

	return 0;

	/*if(N > 1) {
		for(int i = 0 ; i < N;i++) {
			for(int j = 0; j < M; j++){
				if(arr[i][j] < arr[i][j + 1]){

				} else if(arr[i][j] < arr[i + 1][j]){
				
				}
			}
		}
	}*/
	
}


int main()
{

	freopen("D://Source//C++//GCJB//Debug//B-small-attempt2.in", "rt", stdin);
	freopen("D://Source//C++//GCJB//Debug//output.txt", "wt", stdout);

	int testCases = 0;
	

	cin>>testCases;
	

	for (int t = 0; t < testCases; t++) {

		cin>>N;
		cin>>M;
	

		arr = new int*[N];
		for(int i = 0; i < N; ++i){
			arr[i] = new int[M];
		}

		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				cin>>arr[i][j];	
			}
		}

		
		// solution
		int result = check();
		if(result < 0) {
			cout<<"Case #"<<(t+1)<<": NO"<<endl;
		} else {
			cout<<"Case #"<<(t+1)<<": YES"<<endl;
		}


		delete []arr;
	}


	return 0;
}