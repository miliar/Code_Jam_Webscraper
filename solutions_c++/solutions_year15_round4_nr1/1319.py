#include<iostream>
#include<fstream>
using std::cout;
using std::endl;
char arr[100][100];
int R, C;
bool checkUp(int i, int j){
	bool s = false;
	for (int k = i - 1; k >= 0; k--){
		if (arr[k][j] != '.'){
			return true;
		}
	}
	return false;
}
bool checkDown(int i, int j){
	bool s = false;
	for (int k = i + 1; k < R; k++){
		if (arr[k][j] != '.'){
			return true;
		}
	}
	return false;
}
bool checkLeft(int i, int j){
	bool s = false;
	for (int k = j - 1; k >= 0; k--){
		if (arr[i][k] != '.'){
			return true;
		}
	}
	return false;
}
bool checkRight(int i, int j){
	bool s = false;
	for (int k = j + 1; k < C; k++){
		if (arr[i][k] != '.'){
			return true;
		}
	}
	return false;
}

int main(){
	std::ifstream fin;

	std::ofstream fout;
	fin.open("A-large.in", std::ios_base::in);
	fout.open("A-large.out.txt", std::ios_base::trunc);
	int T;
	fin >> T;

	for (int times = 1; times <= T; times++){
		//int R, C;
		fin >> R >> C;
		int size = R*C;
		fin.get();
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				 arr[i][j]=fin.get();
			}
			fin.get();
		}
		int ans = 0, idx = 0;
		bool impossible = false;
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				idx = -1;
				switch (arr[i][j]){
				case '^':
					if (checkUp(i,j))break;
					if (checkDown(i, j)){ ans++; break; }
					if (checkLeft(i, j)){ ans++; break; }
					if (checkRight(i, j)){ ans++; break; }
					impossible = true;
					break;
				case '>':
					if (checkRight(i, j))break;
					if (checkLeft(i, j)){ ans++; break; }
					if (checkUp(i, j)){ ans++; break; }
					if (checkDown(i, j)){ ans++; break; }
					impossible = true;
					break;
				case 'v':
					if (checkDown(i, j))break;
					if (checkUp(i, j)){ ans++; break; }
					if (checkRight(i, j)){ ans++; break; }
					if (checkLeft(i, j)){ ans++; break; }
					impossible = true;
					break;
				case '<':
					if (checkLeft(i, j))break;
					if (checkRight(i, j)){ ans++; break; }
					if (checkDown(i, j)){ ans++; break; }
					if (checkUp(i, j)){ ans++; break; }
					impossible = true;
					break;
				}
				if (impossible)break;
			}
			if (impossible)break;
		}

		//
		if (impossible){
			fout << "Case #" << times << ": " <<"IMPOSSIBLE" << "\n"; 
			std::cout << "IMPOSSIBLE";
		}
		else fout << "Case #" << times << ": " << ans << "\n";
		std::cout << ans << std::endl;
	}
	fin.close();
	fout.close();
	system("PAUSE");
	return EXIT_SUCCESS;
}