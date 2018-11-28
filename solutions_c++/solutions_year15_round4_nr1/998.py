#include <iostream>
#include <fstream>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out;
	out.open("A-large.out");

	int t; 
	in >> t; 
	int r, c;
	for(int i = 0; i < t; i++) {
		int num = 0;
		bool solvable = true;
		in >> r >> c;
		string row_in;
		vector< vector<int> > v;
		bool checked[r][c];
		for(int p = 0; p < r; p++){
			vector<int> row;
			in >> row_in;
			for(int q = 0; q < c; q++) {
				switch(row_in[q]){
					case '.':
						row.push_back(0);
						break;
					case '^':
						row.push_back(1);
						break;
					case '>':
						row.push_back(2);
						break;
					case 'v':
						row.push_back(3);
						break;
					case '<':
						row.push_back(4);
						break;
					default:
						cerr << "reading input failed" <<endl;
				}
				checked[p][q] = false;

			}
			v.push_back(row);
		}
	// . = 0, ^ = 1, > = 2, v = 3, < = 4
		for(int p = 0; p < r; p++){
			for(int q = 0; q < c; q++) {
				int tx = p;
				int ty = q;
				if(v[p][q] == 0)
					continue;
				else if(v[p][q] == 1) {
					bool good = false;
					tx--;
					while(tx >= 0) {
						if(v[tx][ty] != 0){
							good = true;
							break;
						}
						tx--;
					}
					if(!good) {
						num++;
						//search other 3 direction
						tx = p+1; ty = q;
						while(tx < r) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx++;
						}
						tx = p; ty = q-1;
						while(ty >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty--;
						}
						tx = p; ty = q+1;
						while(ty < c) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty++;
						}
					}
					if(!good){
						solvable = false;
					}
				}
				else if(v[p][q] == 2) {
					bool good = false;
					ty++;
					while(ty < c) {
						if(v[tx][ty] != 0){
							good = true;
							break;
						}
						ty++;
					}
					if(!good) {
						num++;
						//search other 3 direction
						tx = p+1; ty = q;
						while(tx < r) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx++;
						}
						tx = p; ty = q-1;
						while(ty >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty--;
						}
						tx = p-1; ty = q;
						while(tx >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx--;
						}
					}
					if(!good){
						solvable = false;
						break;
					}
				}
				else if(v[p][q] == 3) {
					bool good = false;
					tx++;
					while(tx < r) {
						if(v[tx][ty] != 0){
							good = true;
							break;
						}
						tx++;
					}
					if(!good) {
						num++;
						//search other 3 direction
						tx = p-1; ty = q;
						while(tx >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx--;
						}
						tx = p; ty = q-1;
						while(ty >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty--;
						}
						tx = p; ty = q+1;
						while(ty < c) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty++;
						}
					}
					if(!good){
						solvable = false;
					}
				}
				else if(v[p][q] == 4) {
					bool good = false;
					ty--;
					while(ty >= 0) {
						if(v[tx][ty] != 0){
							good = true;
							break;
						}
						ty--;
					}
					if(!good) {
						num++;
						//search other 3 direction
						tx = p+1; ty = q;
						while(tx < r) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx++;
						}
						tx = p-1; ty = q;
						while(tx >= 0) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							tx--;
						}
						tx = p; ty = q+1;
						while(ty < c) {
							if(v[tx][ty] != 0){
								good = true;
								break;
							}
							ty++;
						}
					}
					if(!good){
						solvable = false;
					}
				}
				else {
					cerr<<"None of the cases fits in!" << endl;
				}
			}
		}
		if(solvable)	
			out << "Case #" << i+1 << ": " << num << endl;
		else {
			out << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	out.close();
	return 0;
}

/**
				while(1) {
					if(checked[p][q])
						break;
					if(dir == -1 && v[p][q] == 0){
						checked[p][q] = true;
						break;
					}
				}
*/
