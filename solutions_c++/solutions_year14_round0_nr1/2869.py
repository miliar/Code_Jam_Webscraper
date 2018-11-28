#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	int tests;
	cin >> tests;
	for(int caseNum = 1; caseNum <= tests; caseNum++) {
		int whichRow[2];
		int arr[2][4][4];
		bool isCandidate[2][17];
		vector<int> candidates;

		for(int i=0; i<2; i++) {
			cin >> whichRow[i];
			for(int row=0; row<4; row++) {
				for(int col=0; col<4; col++) {
					int& num = arr[i][row][col];
					cin >> num;
					if(row+1 == whichRow[i])
						isCandidate[i][num] = true;
					else
						isCandidate[i][num] = false;
				}
			}
		}

		for(int num=1; num<=16; num++) {
			if(isCandidate[0][num] && isCandidate[1][num])
				candidates.push_back(num);
		}

		cout << "Case #" << caseNum << ": ";
		if(candidates.size() == 1)
			cout << candidates[0];
		else if(candidates.size() > 1)
			cout << "Bad magician!";
		else if(candidates.size() == 0)
			cout << "Volunteer cheated!";
		cout << endl;
	}	
	return 0;
}