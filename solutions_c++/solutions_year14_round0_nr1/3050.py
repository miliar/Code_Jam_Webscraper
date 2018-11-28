#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int cards_1[4][4];
int cards_2[4][4];

string solve(int first, int second) {
	int duplicates = 0;
	int num;
	for(int col1 = 0; col1 < 4; col1++) {
		for(int col2 = 0; col2 < 4; col2++) {
			int n1 = cards_1[first - 1][col1];
			int n2 = cards_2[second - 1][col2];
			if(n1 == n2) {
				duplicates++;
				num = n1;
			}
		}
	}
	ostringstream ss;
	ss << num;
	if(duplicates == 0) return "Volunteer cheated!";
	if(duplicates == 1) return ss.str();
	if(duplicates > 1) return "Bad magician!";
}

int main(void) 
{
	int TC;
	cin >> TC;
	for(int tc = 0; tc < TC; tc++) {
		int first_ans;
		cin >> first_ans;
		for(int row = 0; row < 4; row++) {
			for(int col = 0; col < 4; col++) {
				cin >> cards_1[row][col];
			}
		}
		int second_ans;
		cin >> second_ans;
		for(int row = 0; row < 4; row++) {
			for(int col = 0; col < 4; col++) {
				cin >> cards_2[row][col];
			}
		}
		cout << "Case #" << (tc + 1) << ": " << solve(first_ans, second_ans) << endl;
	}
	return 0;
}
