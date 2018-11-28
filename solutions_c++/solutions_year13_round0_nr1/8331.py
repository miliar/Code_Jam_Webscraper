#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	char grid[16];
	int num;
	string outstr[5] = {"", "X won", "O won", "Game has not completed", "Draw"};
	fin>>num;
	for (int n = 0; n < num; n++){
		int out = 0;
		for (int i = 0; i < 16; i++){
			fin>>grid[i];
			if (grid[i] == '.'){
				out = 3;
			}
		}
		int d1x = 0;
		int d1y = 0;
		int d2x = 0;
		int d2y = 0;
		for (int i = 0; i < 4; i++){
			int rx = 0;
			int ry = 0;
			int cx = 0;
			int cy = 0;
			if (grid[i*4+i] == 'X'){
				d1x +=1;
			}
			else if (grid[i*4+i] == 'O'){
				d1y +=1;
			}
			else if (grid[i*4+i] == 'T'){
				d1x +=1;
				d1y +=1;
			}
			if (grid[(i+1)*3] == 'X'){
				d2x +=1;
			}
			else if (grid[(i+1)*3] == 'O'){
				d2y +=1;
			}
			else if (grid[(i+1)*3] == 'T'){
				d1x +=1;
				d2y +=1;
			}
			for (int j = 0; j < 4; j++){
				if (grid[i*4+j] == 'X'){
					rx += 1;
				}
				else if (grid[i*4+j] == 'O'){
					ry += 1;
				}
				else if (grid[i*4+j] == 'T'){
					ry += 1;
					rx += 1;
				}
				if (grid[j*4+i] == 'X'){
					cx += 1;
				}
				else if (grid[j*4+i] == 'O'){
					cy += 1;
				}
				else if (grid[j*4+i] == 'T'){
					cx += 1;
					cy += 1;
				}
			}
			if ((rx > 3) || (cx > 3)){
				out = 1;
				break;
			}
			if ((ry > 3) || (cy > 3)){
				out = 2;
				break;
			}
		}
		if ((d1x > 3) || (d2x > 3)){
			out = 1;
		}
		if ((d1y > 3) || (d2y > 3)){
			out = 2;
		}
		if ((out != 1) && (out != 2) && (out != 3)){
			out = 4;
		}
		if (out!=0)
			fout<<"Case #"<<n+1<<": "<<outstr[out]<<endl;
	}
	return 0;
}