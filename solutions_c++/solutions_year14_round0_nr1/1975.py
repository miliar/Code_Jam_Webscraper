#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int r1, r2, temp;
		vector<int> row1, row2;

		cin >> r1;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				cin >> temp;
				if (r1 == i + 1)
					row1.push_back(temp);
			}
		}

		cin >> r2;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				cin >> temp;
				if (r2 == i + 1)
					row2.push_back(temp);
			}
		}

		int count = 0;
		int val;
		for (int i=0;i<row1.size();i++) {
			for (int j=0;j<row2.size();j++) {
				if (row1[i] == row2[j]) {
					count++;
					val = row1[i];
					break;
				}
			}
		}

		cout << "Case #" << (q + 1) << ": ";

		if (count == 1) {
			cout << val;
		}
		else if (count == 0) {
			cout << "Volunteer cheated!";
		}
		else {
			cout << "Bad magician!";
		}

		cout << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}