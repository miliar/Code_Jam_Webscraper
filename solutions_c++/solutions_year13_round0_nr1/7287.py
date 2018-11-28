#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

void print(int z, string tmp) { cout << "Case #" << z << ": " << tmp << endl; }

bool check(int z, string M)
{
	int x = 0, o = 0, t = 0;
	for (int i = 0; i < 4; i++)
		if (M[i] == 'X') x++;
	for (int i = 0; i < 4; i++)
		if (M[i] == 'O') o++;
	for (int i = 0; i < 4; i++)
		if (M[i] == 'T') t++;
	if (x == 4 || (x==3 && t==1)){
		print(z,"X won");
		return true;
	} else if (o == 4 || (o==3&&t==1)){
		print(z,"O won");
		return true;
	} else {
		return false;
	}
}


int main()
{
	int T, x, o;
	bool next;
	vector<string> M(4,"");
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		next = false;
		for (int i = 0; i < 4; i++)
			cin >> M[i];
		//rows
		for (int i = 0; i < 4; i++){
			if (check(z,M[i])){
				next = true;
				break;
			}
		}
		if (next) continue;
		
		//cols
		for (int i = 0; i < 4; i++){
			string tmp = "";
			for (int j = 0; j < 4; j++){
				tmp += M[j][i];
			}
			if (check(z,tmp)){
				next = true;
				break;
			}
		}
		if (next) continue;

		//diagonals
		stringstream tmp;
		tmp << M[0][0] << M[1][1] << M[2][2] << M[3][3];
		if (check(z,tmp.str()))
			continue;

		stringstream tmp1;
		tmp1 << M[0][3] << M[1][2] << M[2][1] << M[3][0];
		if (check(z,tmp1.str()))
			continue;
		
		//draw
		for (int i = 0; i < 4 && (!next); i++){
			for (int j =0; j < 4; j++)
				if (M[i][j] == '.')
				{
					print(z,"Game has not completed");
					next = true;
					break;
				}
			if (next) break;
		}
		if (next) continue;
		print(z,"Draw");
	}
	return 0;
}

