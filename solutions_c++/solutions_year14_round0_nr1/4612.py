#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <fstream>

using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
	ifstream fin("input1.in");
	ofstream fout("out.txt");
	int n;
	int i, j, k, l;
	fin >> n;

	vector<vector<int> > matrix(4, vector<int>(4, 0));
	vector<int> row1(4, 0);
	vector<int> row2(4, 0);

	for(i = 0; i < n; i++) {
		int num;
		int item;
		int firstRow, secRow;

		fin >> firstRow;
		for (j = 0; j < 4; j++) {
			for(k = 0; k < 4; k++) {
				fin >> item;
				matrix[j][k] = item;
			}
		}

		for(j = 0; j < 4; j++) {
			row1[j] = matrix[firstRow-1][j];
			//cout << row1[j] << ' ';
		}
		//cout << endl;

		fin >> secRow;
		for (j = 0; j < 4; j++) {
			for(k = 0; k < 4; k++) {
				fin >> item;
				matrix[j][k] = item;
			}
		}

		for(j = 0; j < 4; j++) {
			row2[j] = matrix[secRow-1][j];
			//cout << row2[j] << ' ';
		}
		//cout << endl;

		int cnt = 0;
		int key = -1;
		for(j = 0; j < 4; j++){
			for(k = 0; k < 4; k++){
				if(row1[j] == row2[k]){
					cnt++;
					key = row1[j];
				}
				//cout <<"key: " << key << endl; 
			}
		}
		
		fout << "Case #" << i+1 << ": ";
		if(cnt == 0) fout << "Volunteer cheated!" << endl;
		if(cnt > 1) fout << "Bad magician!" << endl;
		if(cnt == 1) fout << key << endl;;
	}

	fout.close();
	fin.close();
	
    return 0;
}
