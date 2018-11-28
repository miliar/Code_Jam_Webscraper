#include <iostream>
#include <fstream>

using namespace std;


int map[101][101];
int map2[101][101];
int n;
int m1, m2;

ifstream fin("input.txt");
ofstream fout("output.txt");

void input1()
{
	for (int i = 0; i<4;i++){
		for (int j = 0; j < 4; j++){
			fin >> map[i][j];
		}
	}

}

void input2(){

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			fin >> map2[i][j];
		}
	}
}

void proc(int c){
	m1--;
	m2--;
	int i, j;
	int cnt = 0;

	for (i = 0; i < 4; i++){
		for (j = 0; j < 4; j++){
			if (map[m1][i] == map2[m2][j]){
				cnt++;
			}
		}
	}
	if (cnt > 1){
		fout << "Case #" << c + 1 << ": " << "Bad magician!" << endl;
		return;
	}
	else if (cnt == 0){
		fout << "Case #" << c + 1 << ": " << "Volunteer cheated!" << endl;
		return;
	}

	for (i = 0; i < 4; i++){
		for (j = 0; j < 4; j++){
			if (map[m1][i] == map2[m2][j]){
				fout << "Case #" << c + 1 << ": " << map[m1][i] << endl;
				return;
			}
		}

	}




	
}
void main()
{
	fin >> n;
	for (int i = 0; i < n; i++){
		memset(map, 0, sizeof(map));
		memset(map2, 0, sizeof(map2));
		fin >> m1;
		input1();
		fin >> m2;
		input2();
		proc(i);
	}
}