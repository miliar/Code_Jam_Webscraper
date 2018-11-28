#include <iostream>
#include <vector>
using namespace std;

int main() {
	int tests;
	int answer_one;
	int answer_two;
	int n;
	int row;
	int num;
	vector<int> matrix;
	vector<int> result;
	
	cin >> tests;
	
	for(int x = 1; x < tests + 1; x++) {
		cin >> answer_one;
		for(int y = 0; y < 16; y++) {
			cin >> n;
			matrix.push_back(n);
		}
		
		cin >> answer_two;
		for(int y = 0; y < 16; y++) {
			cin >> n;
			matrix.push_back(n);
		}
		for(int y = 0; y < 4; y++) {
			row = matrix[(answer_one * 4) - 4 + y];
			for(int z = 0; z < 4; z++) {
				num = matrix[16 + (answer_two * 4) - 4 + z];
				if(row == num) {
					result.push_back(num);
				}
			}
		}
		switch (result.size()) {
			case 0: cout << "Case #" << x << ": " << "Volunteer cheated!" << endl;
				break;
			case 1: cout << "Case #" << x << ": " << result[0] << endl;
				break;
			default: cout << "Case #" << x << ": " << "Bad magician!" << endl;
				break;
			
		}
		result.clear();
		matrix.clear();
		
	}
	
	return 0;
}