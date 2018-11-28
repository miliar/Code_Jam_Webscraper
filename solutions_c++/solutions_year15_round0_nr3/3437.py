#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int chartable[4][4] = { { 1, 2, 3, 4 },
{ 2, -1, 4, -3 },
{ 3, -4, -1, 2 },
{ 4, 3, -2, -1 } };

int full = 0;

ifstream ifs;
ofstream ofs;

int tonum(char c){
	if (c == 'i')
		return 2;
	if (c == 'j')
		return 3;
	if (c == 'k')
		return 4;
}

int mult(int a, int b) {
	return chartable[abs(a) - 1][abs(b) - 1] * a / abs(a) * b / abs(b);
}

int multup(int from, int to, vector<int> &str){
	int num = 1;
	for (int i = from; i < to; i++){
		num = mult(num, str[i]);
	}
	return num;
}

void solve(vector<int> &str, int iter){
	int num = 1;
	int state = 0;
	int found = false;
	for (int ii = 0; ii < iter; ii++ ){
		for (int i = 0; i < str.size(); i++){
			int newnum = 0;
			switch (state){
			case 0:
				newnum = mult(num, str[i]);
				if (newnum == 2){
					state = 1;
					num = 1;
				}
				else
					num = newnum;
				break;
			case 1:
				newnum = mult(num, str[i]);
				if (newnum == 3){
					state = 2;
					num = 1;
				}
				else
					num = newnum;
				break;
			case 2:
				newnum = mult(num, str[i]);
				if (newnum == 4){
					int rest = multup(i + 1, str.size(), str);
					for (int j = 1; j < iter-ii; j++){
						rest = mult(rest, full);
					}
					if (rest == 1)
						ofs << "YES" << endl;
					else
						ofs << "NO" << endl;
					ii = iter;
					i = str.size();
					found = true;
				}
				else
					num = newnum;
				break;
			default:
				break;
			}
		}
	}
	if ( !found )
		ofs << "NO" << endl;
}

int main(int argc, char **argv) {
	ifs.open(argv[1]);
	ofs.open("output.out");
	int T;
	ifs >> T;
	for (int ccc = 1; ccc <= T; ccc++){
		int L, X;
		ifs >> L >> X;
		string input;
		ifs >> input;
		vector<int> vals(L);
		for (int i = 0; i < input.size(); i++){
			vals[i] = tonum(input[i]);
		}
		full = multup(0, vals.size(), vals);
		ofs << "Case #" << ccc << ": ";
		solve(vals, X);
	}
	return 0;
}
