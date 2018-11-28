#include<iostream>
#include<sstream>
#include<vector>
#include<fstream>

using namespace std;

vector<int> trick(int a);
vector<int> trick(int a) {
// Make the grid
	int c;
	int grid[4][4];
	for (int i = 0; i < 4; i++) {
		for (int j = 0 ; j < 4; j++) {
			cin >> c;
			grid[i][j] = c;
		}
	}
// Checking the cards
	vector<int> a1;
	for (int i = 0; i < 4; i++) {
		a1.push_back(grid[a-1][i]);
	}
	return a1;
}
int main() {
//	ifstream infile;
//	infile.open("A-small-attempt0.in");
//	ofstream outfile;
//	outfile.open("output.txt");
	int a , b , b1 , c , count , card , iteration;
	cin >> a;
	iteration = 0;
	for (int i = 0; i < a; i++) {
		iteration++;
		cin >> b;
		vector<int> first_arrangement = trick(b);
		cin >> b1;
		vector<int> second_arrangement = trick(b1);
		count = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (first_arrangement[i] == second_arrangement[j]) {
					card = first_arrangement[i];
					count++;
				}		
			}
		}
		if (count == 1) {
			cout << "Case #" << iteration << ": " << card << endl;
		} else if (count > 1) {
			cout << "Case #" << iteration << ": Bad Magician!" << endl;
		} else if (count == 0) {
			cout << "Case #" << iteration << ": Volunteer Cheated!" << endl;
		}	
	}
//	infile.close();
//	outfile.close();

return 0;
}


