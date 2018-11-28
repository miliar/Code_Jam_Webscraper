#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string name[] = {"GABRIEL" , "RICHARD"};

int main(){
	ifstream fin("ominoe.in"); ofstream fout("ominoe.out");

	int T;
	fin >> T;
	for(int i = 1; i <= T; ++i){
		int x, r, c, win;
		fin >> x >> r >> c;
		if(r*c%x) win = 1;
		else if(c < x && r < x) win = 1;
		else if(c+1 < x || r+1 < x) win = 1;
		else win = 0;
		fout << "Case #"<<i<<": "<<name[win]<<endl;
	}
	return 0;
}
