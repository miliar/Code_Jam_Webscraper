#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

int mat[100][100];
int lin,col;

bool checalinha(int i, int j, int linha) {
	for(int k=0;k<col;k++) {
		if(mat[i][j] < mat[linha][k]) return false;
	}
	return true;
}

bool checacoluna(int i, int j, int coluna) {
	for(int k=0;k<lin;k++) {
		if(mat[i][j] < mat[k][coluna]) return false;
	}
	return true;	
}

bool possivel(int i, int j) {
	if(checalinha(i,j,i) || checacoluna(i,j,j)) return true;
}
		
int main() {
	int T;
	cin >> T;
	int C = 1;
	while(T-- > 0) {
		int n,m;
		cin >> n >> m;
		lin = n; col = m;
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				cin >> mat[i][j];
			}
		}
		
		bool resp = true;
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(!possivel(i,j)) { resp = false; break; break; }
			}
		}
		
		if(resp) cout << "Case #" << C++ << ": YES"<<endl;
		else cout << "Case #" << C++ << ": NO"<<endl;
		
	}
	return 0;
}

