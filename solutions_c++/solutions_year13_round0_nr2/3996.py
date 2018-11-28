#include <iostream>
#include <fstream>

using namespace std;
ofstream mycout;

int rowMaximum(int **pattern, int r, int N, int M){
	int max = pattern[r][0];
	for(int i = 1; i < M; i++){
		if( pattern[r][i] > max )
			max = pattern[r][i];
	}
	return max;
}

int columnMaximum(int **pattern, int c, int N, int M){
	int max = pattern[0][c];
	for(int i = 1; i < N; i++){
		if(pattern[i][c] > max)
			max = pattern[i][c];
	}
	return max;
}

void relaxrow(int **lawn, int r, int N, int M, int value){		
	for(int i = 0; i < M; i++){
		if(lawn[r][i] > value)
			lawn[r][i] = value;
	}
}

void relaxcolumn(int **lawn, int c, int N, int M, int value){
	for(int i = 0; i < N; i++){
		if(lawn[i][c] > value)
			lawn[i][c] = value;
	}
}

void restoreLawn(int **lawn, int N, int M){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			lawn[i][j] = 100;
		}
	}
}
int finalcheck(int **lawn, int **pattern, int N, int M){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(lawn[i][j] != pattern[i][j])
				return 0;
		}
	}
	return 1;
}

int strategy(int **lawn, int **pattern, int N, int M){
	for(int i = 0; i < N; i++){
		int value = rowMaximum(pattern, i, N, M);
		//cout << "i: " << i << " max row value: " << value << endl;
		relaxrow(lawn, i, N, M, value);
	}
	for(int i = 0; i < M; i++){
		int value = columnMaximum(pattern, i, N, M);
		//cout << "i: " << i << " max column value: " << value << endl;
		relaxcolumn(lawn, i, N, M, value);
	}
	int check = finalcheck(lawn, pattern, N, M);
	return check;
}

int strategy1(int **lawn, int **pattern, int N, int M){
	for(int i = 0; i < N; i++){
		if(pattern[i][0] < lawn[i][0]){
			relaxrow(lawn, i, N, M, pattern[i][0]);
		}
	}
	
	for(int i = 1; i < M; i++){
		if(pattern[0][i] < lawn[0][i])
			relaxcolumn(lawn, i, N, M, pattern[0][i]);
	}
	
	for(int i = M-1; i > 0; i--){
		if(pattern[N-1][i] < lawn[N-1][i])
			relaxcolumn(lawn, i, N, M, pattern[N-1][i]);
	}
	
	int check = finalcheck(lawn, pattern, N, M);
	return check;
}

int strategy2(int **lawn, int **pattern, int N, int M){

	
	for(int i = 0; i < M; i++){
		if(pattern[0][i] < lawn[0][i])
			relaxcolumn(lawn, i, N, M, pattern[0][i]);
	}
	
	for(int i = 1; i < N; i++){
		if(pattern[i][0] < lawn[i][0]){
			relaxrow(lawn, i, N, M, pattern[i][0]);
		}
	}	
	for(int i = 1; i < N; i++){
		if(pattern[i][M-1] < lawn[i][M-1]){
			relaxrow(lawn, i, N, M, pattern[i][0]);
		}
	}
	
	int check = finalcheck(lawn, pattern, N, M);
	return check;
}

void freeMemory(int** lawn, int** pattern, int N, int M){
	for(int i = 0; i < N; i++){
		free(lawn[i]);
		free(pattern[i]);
	}
	free(lawn);
	free(pattern);
}
void process(int testcase){
	int N, M;
	cin >> N;
	cin >> M;
	
	int **lawn, **pattern;
	lawn = (int**)malloc(N*sizeof(int*));
	pattern = (int**)malloc(N*sizeof(int*));
	
	for(int i = 0; i < N; i++){
		lawn[i] = (int*)malloc(M*sizeof(int));
		pattern[i] = (int*)malloc(M*sizeof(int));
	}
	
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			lawn[i][j] = 100;
			cin >> pattern[i][j];
		}
	}
	mycout << "Case #" << testcase << ": ";
	/*
	int check = strategy1(lawn, pattern, N, M);
	if(check)
		mycout << "YES" << endl;
	else{
		restoreLawn(lawn, N, M);
		int check1 = strategy2(lawn, pattern, N, M);
		if(check1)
			mycout << "YES" << endl;
		else
			mycout << "NO" << endl;
	}
	*/
	
	int check = strategy(lawn, pattern, N, M);
	if(check)
		mycout << "YES" << endl;
	else
		mycout << "NO" << endl;
	
	freeMemory(lawn, pattern, N, M);
}

int main(){
	int T;
	cin >> T;
	
	mycout.open("output1.txt");
	for(int i = 0; i < T; i++){
		process(i+1);
	}
	mycout.close();
}
