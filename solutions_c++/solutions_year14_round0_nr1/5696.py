#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;



int main() {
	int T;
	cin >> T;
	ofstream out("MagicTrick.txt");
	for (int idx = 1; idx <= T; idx++) {
		int row;
		vector<int> v1(4), v2(4);
		vector< vector<int> > temp(4);

		cin >> row;
		for (int i = 0; i < 4; i++) {
			temp[i].resize(4);
			for (int j = 0; j < 4; j++) 
				cin >> temp[i][j];
		}
		v1 = temp[row-1];
		cin >> row;
		for (int i = 0; i < 4; i++) {
			temp[i].resize(4);
			for (int j = 0; j < 4; j++) 
				cin >> temp[i][j];
		}
		v2 = temp[row-1];

		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());

		vector<int> result(4);
		vector<int>::iterator it;
		it = set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),result.begin());
		result.resize(it-result.begin());


		if (result.size() == 0)
			out << "Case #" << idx << ": Volunteer cheated!";
		else if (result.size() == 1)
			out << "Case #" << idx << ": " << result[0];
		else
			out << "Case #" << idx << ": Bad magician!";

		if (idx != T) out << endl;

	}
	out.close();
	return 0;
}