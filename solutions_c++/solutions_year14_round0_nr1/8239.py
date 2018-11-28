#include <iostream>
#include <set>
#include <vector>
#include <assert.h>
using namespace std;

int main()
{
	int nCases = 0;
	cin >> nCases;
	for (int n = 0; n < nCases; n++) {
		// read first row
		int firstRowIndex;
		cin >> firstRowIndex;
		vector<int> firstRow;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int curr;
				cin >> curr;
				if (i == firstRowIndex - 1) {
					firstRow.push_back(curr);
				}
			}
		}
		// read second row
		int secondRowIndex;
		cin >> secondRowIndex;
		set<int> secondRow;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int curr;
				cin >> curr;
				if (i == secondRowIndex - 1) {
					secondRow.insert(curr);
				}
			}
		}
		// find intersection
		int nIntersections = 0;
		int lastIntersection = -1;
		for each (int item in firstRow)
		{
			if (secondRow.find(item) != secondRow.end()) {
				nIntersections++;
				lastIntersection = item;
			}
		}
		// output result
		cout << "Case #" << n + 1 << ": ";
		switch (nIntersections) {
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		case 1:
			cout << lastIntersection << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
			break;
		}
	}
}


