#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int t, x, r, c;

int main(){
	fstream fin("D.in");
	fstream fout("D.out");
	fin >> t;
	bool win;
	for(int i = 1; i <= t; ++i){
		win = false;
		fin >> x >> r >> c;
		if(x == 1) win = true;
		if(x == 2) if((r*c)%2 == 0) win = true;
		if(x == 3){
			if((r*c)%3 == 0){
				if(r*c == 6) win = true;
				if(r*c == 9) win = true;
				if(r*c == 12) win = true;
			}
		}
		if(x == 4){
			if((r*c)%4 == 0){
				if(r*c == 12) win = true;
				if(r*c == 16) win = true;
			}
		}
		
		fout << "Case #" << i << ": ";
		if(win) fout << "GABRIEL" << endl;
		else fout << "RICHARD" << endl;
	}
	return 0;
}
