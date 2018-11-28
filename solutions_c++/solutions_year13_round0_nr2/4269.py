/*
 * main.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: michael
 */
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <unistd.h>

using namespace std;

bool checkRow(int ** lawn, int r, int cols, int h){
	for (int i=0; i<cols; i++){
		if (lawn[r][i] > h)
			return false;
	}
	return true;
}

bool checkCol(int ** lawn, int c, int rows, int h){
	for (int i=0; i<rows; i++){
		if (lawn[i][c] > h)
			return false;
	}
	return true;
}

int main(){
	char buffer[20];
	int numCases;

	cin.getline(buffer, 20);
	sscanf(buffer, "%d", &numCases);
	for (int i = 0; i < numCases; i++) {
		int N = 0, M = 0;
		memset(buffer, 0, 20);
		cin.getline(buffer, 20);
		sscanf(buffer,"%i %i",&N,&M);
		int ** lawn;
		lawn = new int*[N];
		for (int n=0; n<N; n++){
			lawn[n] = new int[M];
		}
		for (int n=0; n<N; n++){
			for (int m=0; m<M; m++){
				cin >> lawn[n][m];
			}
		}
		for (int n=0; n<N; n++){
			for (int m=0; m<M; m++){
			}
		}
		bool status = true;
		for (int n=0; n<N; n++){
			for (int m=0; m<M; m++){
				int h = lawn[n][m];
				if (!checkRow(lawn,n,M,h) && !checkCol(lawn,m,N,h)){
					status = false;
				}
			}
		}
		if (status)
			printf("Case #%i: YES\n", i+1);
		else
			printf("Case #%i: NO\n", i+1);
		cin.getline(buffer, 20);

	}

	return 0;
}



