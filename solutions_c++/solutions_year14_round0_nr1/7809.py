#include <iostream>
#include <unordered_set>
using namespace std;
int main() {
	int T;
	cin >> T;
	for(int i=1; i<=T; i++) {
		unordered_set<int> set;
		int r1;
		cin >> r1;
		int c[4][4];
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++)
				cin >> c[j][k];
		}
		for(int j=0; j<4; j++)
			set.insert(c[r1 - 1][j]);
		int r2;
		cin >> r2;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++)
				cin >> c[j][k];
		}
		int count = 0, result;
		for(int j=0; j<4; j++) {
			if(set.find(c[r2 - 1][j]) != set.end()) {
				count ++;
				result = c[r2 - 1][j];
			}
		}
		cout << "Case #" << i << ": ";
		if(count == 0)
			cout << "Volunteer cheated!";
		else if(count == 1)
			cout << result;
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
