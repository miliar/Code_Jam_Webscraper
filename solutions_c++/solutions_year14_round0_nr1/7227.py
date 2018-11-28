#include <iostream>
#include <fstream>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <map>
#include <algorithm>
#include <assert.h>


#include <math.h>

#define BAD_MAGICIAN -1
#define VOLUNTEER_CHEATED -2

using namespace std;

typedef vector<int> Row;
typedef vector<Row> Grid;

vector<int> strToIntVector(string v);

void printVector(vector<int> v) {
	int i;
	for (i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

class TestCase {
	private:
		Grid grid1;
		Grid grid2;
		int row1;
		int row2;

	public:
		TestCase(int row1, int row2, vector<string> grid1, vector<string> grid2) {
			this->row1 = row1;
			this->row2 = row2;
			this->grid1 = gridFromStrings(grid1);
			this->grid2 = gridFromStrings(grid2);
		}

		static Grid gridFromStrings(vector<string> rows) {
			Grid g;
			int i;
			for (i = 0; i < rows.size(); i++) {
				g.push_back(strToIntVector(rows[i]));	
			}
			return g;
		}

		int getSelectedCard() {
			int i, card;
			vector<int> common;

			for (i = 0; i < grid1[row1].size(); i++) {
				if (find(grid2[row2].begin(), grid2[row2].end(), grid1[row1][i]) != grid2[row2].end()) {
					common.push_back(grid1[row1][i]);
				}
			}

			switch(common.size()) {
				case 0:
					card = VOLUNTEER_CHEATED;
					break;
				case 1:
					card = common[0];
					break;
				default:
					card = BAD_MAGICIAN;
					break;
			}
			return card;
		}

};

vector<TestCase> readFile(char* filename) {
	vector<TestCase> cases;
	ifstream infile(filename);
	string line;

	if (infile.is_open()) {
		getline(infile,line);
		int r, c, t, T = atoi(line.c_str());
		vector<int> row1, row2;
		
		for (t = 0; t < T; t++) {
			getline(infile,line);
			row1 = strToIntVector(line);
			vector<string> grid1;
			for (r = 0; r < 4; r++) {
				getline(infile,line);
				grid1.push_back(line);
			}

			getline(infile,line);
			row2 = strToIntVector(line);
			vector<string> grid2;
			for (r = 0; r < 4; r++) {
				getline(infile,line);
				grid2.push_back(line);
			}


			TestCase tCase(row1[0]-1, row2[0]-1, grid1, grid2);
		
			cases.push_back(tCase);
		}

		infile.close();
	}
	else { 
		perror("open"); 
	}

	return cases;
}

vector<int> strToIntVector(string v) {
	vector<int> vec;
	char pointer[strlen(v.c_str()) + 1];
	strcpy(pointer, v.c_str());

	const char* space = " ";
	char* dim = strtok(pointer, space);
	while (dim) {
		vec.push_back(atoi(dim));
		dim = strtok(NULL, space);
	}
	return vec;
}


int main(int argc, char** argv) {
	vector<TestCase> cases = readFile(argv[1]);
	int c;
	string answer;
	for (c = 0; c < cases.size(); c++) {
		int resp = cases[c].getSelectedCard();
		switch(resp) {
			case VOLUNTEER_CHEATED:
				printf("Case #%d: %s\n", c+1,"Volunteer cheated!");
				break;
			case BAD_MAGICIAN:
				printf("Case #%d: %s\n", c+1,"Bad magician!");
				break;
			default:
				printf("Case #%d: %d\n", c+1,resp);
				break;
		}
	}
}









