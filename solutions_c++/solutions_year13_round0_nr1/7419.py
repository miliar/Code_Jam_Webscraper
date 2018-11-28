#include <fstream>

using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("tomek.out");
	int t;
	string m[4];
	fin >> t;
	for(int i = 0; i < t; i++){
		for(int x = 0; x < 4; x++){
			fin >> m[x];
		}
		bool t = false, flag = false;
		int xcount, ocount;
		for(int x = 0; x < 4; x++){
			xcount = 0;
			ocount = 0;
			t = false;
			for(int y = 0; y < 4; y++){
				if(m[x][y] == 'X')
					++xcount;
				else if(m[x][y] == 'O')
					++ocount;
				else if(m[x][y] == 'T')
					t = true;
			}
			if(ocount == 4 || (t && ocount == 3)){
				fout << "Case #" << i + 1 << ": O won" << endl;
				flag = true; break;
			}
			if(xcount == 4 || (t && xcount == 3)){
				fout << "Case #" << i + 1 << ": X won" << endl;
				flag = true; break;
			}
		}
		if(flag)
			continue;
		for(int x = 0; x < 4; x++){
			xcount = 0;
			ocount = 0;
			t = false;
			for(int y = 0; y < 4; y++){
				if(m[y][x] == 'X')
					++xcount;
				else if(m[y][x] == 'O')
					++ocount;
				else if(m[y][x] == 'T')
					t = true;
			}
			if(ocount == 4 || (t && ocount == 3)){
				fout << "Case #" << i + 1 << ": O won" << endl;
				flag = true; break;
			}
			if(xcount == 4 || (t && xcount == 3)){
				fout << "Case #" << i + 1 << ": X won" << endl;
				flag = true; break;
			}
		}
		if(flag)
			continue;
		t = false;
		xcount = 0;
		ocount = 0;
		for(int x = 0; x < 4; x++){
			if(m[x][x] == 'X')
				++xcount;
			else if(m[x][x] == 'O')
				++ocount;
			else if(m[x][x] == 'T')
				t = true;
			if(ocount == 4 || (t && ocount == 3)){
				fout << "Case #" << i + 1 << ": O won" << endl;
				flag = true; break;
			}
			if(xcount == 4 || (t && xcount == 3)){
				fout << "Case #" << i + 1 << ": X won" << endl;
				flag = true; break;
			}
		}
		if(flag)
			continue;
		t = false;
		xcount = 0;
		ocount = 0;
		for(int x = 0; x < 4; x++){
			if(m[x][3-x] == 'X')
				++xcount;
			else if(m[x][3-x] == 'O')
				++ocount;
			else if(m[x][3-x] == 'T')
				t = true;
			if(ocount == 4 || (t && ocount == 3)){
				fout << "Case #" << i + 1 << ": O won" << endl;
				flag = true; break;
			}
			if(xcount == 4 || (t && xcount == 3)){
				fout << "Case #" << i + 1 << ": X won" << endl;
				flag = true; break;
			}
		}
		if(flag)
			continue;
		int empty = 0;
		for(int x = 0; x < 4; x++)
			for(int y = 0; y < 4; y++)
				if(m[x][y] != '.')
					++empty;
		if(empty != 16)
			fout << "Case #" << i + 1 << ": Game has not completed" << endl;
		else
			fout << "Case #" << i + 1 << ": Draw" << endl;
	}
	return 0;
}
