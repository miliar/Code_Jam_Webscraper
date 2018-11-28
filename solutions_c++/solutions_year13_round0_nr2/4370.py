/*
 * lawn.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: grand
 */
#include<iostream>
#include<string>

using namespace std;

int lawn[100][100];

int oldlawn[100][100];

void readLawn(int N, int M) {
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			cin >> lawn[i][j];
			oldlawn[i][j]=100;
		}
}

int max(int a, int b) {
	return a > b ? a : b;
}

void dowork(int N, int M) {
	//do row work
	int max = 0;
	for (int i = 0; i < N; i++) {
		int j = 0;
		max = 0;
		for (j = 0; j < M; j++) {
			if (max == 100)
				break;
			if (lawn[i][j] > max)
				max = lawn[i][j];
		}
		if (max ==100)
			continue;
		for (j = 0; j < M; j++)
			if(oldlawn[i][j]>max)
				oldlawn[i][j]=max;
	}
	//do column work
	for (int j = 0; j < M; j++) {
		int i = 0;
		max = 0;
		for (i = 0; i < N; i++) {
			if (max == 100)
				break;
			if (lawn[i][j] > max)
				max = lawn[i][j];
		}
		if (max ==100)
			continue;
		for (i = 0; i < N; i++){
			if(oldlawn[i][j]>max)
				oldlawn[i][j]=max;
		}
	}
}

bool checkLawn(int N,int M){
	bool ret =true;
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			if(lawn[i][j]!=oldlawn[i][j])
				return false;
	return ret;
}

int main() {
	int T;
	cin >> T;
	int N, M;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		readLawn(N, M);
		dowork(N,M);
		if(checkLawn(N,M))
			cout<<"Case #"<<i+1<<": YES"<<endl;
		else
			cout<<"Case #"<<i+1<<": NO"<<endl;
	}

	return 0;
}

