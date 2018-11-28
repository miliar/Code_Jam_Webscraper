#include <fstream>
#include <vector>

using namespace std;

char eq(char a, char b){
	if(b == 'T'){
		char c = a;
		a = b;
		b = c;
	}
	if((a == 'X' && b == 'X') || (a == 'T' && b == 'X')){
		return 'X';
	}
	if((a == 'O' && b == 'O') || (a == 'T' && b == 'O')){
		return 'O';
	}
	return 0;
}

char eq4(char a, char b, char c, char d){
	if(eq(a, b) && eq(b, c) && eq(c, d) && eq(a, c) && eq(a, d) && eq(b, d)){
		return eq(a, b);
	}
	return 0;
}

int main(){
	ifstream fin("a.in");
	ofstream fout("a.out");
	vector<vector<char> > A(4);
	for(int i = 0; i < 4; i++){
		A[i].resize(4);
	}
	int t;
	fin >> t;
	char ch;
	for(int k = 1; k <= t; k++){
		int point = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				fin >> ch;
				if(ch == '.'){
					point++;
				}
				A[i][j] = ch;
			}
		}
		bool ans = false;
		for(int i = 0; i < 4; i++){
			if(eq4(A[i][0], A[i][1], A[i][2], A[i][3])){
				fout << "Case #" << k <<": " << eq4(A[i][0], A[i][1], A[i][2], A[i][3]) << " won\n";
				ans = true;
				break;
			}
			if(eq4(A[0][i], A[1][i], A[2][i], A[3][i])){
				fout << "Case #" << k <<": " << eq4(A[0][i], A[1][i], A[2][i], A[3][i]) << " won\n";
				ans = true;
				break;
			}
		}
		if(!ans && eq4(A[0][0], A[1][1], A[2][2], A[3][3])){
			fout << "Case #" << k <<": " << eq4(A[0][0], A[1][1], A[2][2], A[3][3]) << " won\n";
			ans = true;
		}
		if(!ans && eq4(A[0][3], A[1][2], A[2][1], A[3][0])){
			fout << "Case #" << k <<": " << eq4(A[0][3], A[1][2], A[2][1], A[3][0]) << " won\n";
			ans = true;
		}
		if(!ans){
			if(point){
				fout << "Case #" << k <<": Game has not completed\n";
			} else {
				fout << "Case #" << k <<": Draw\n";
			}
		}
	}
	return 0;
}