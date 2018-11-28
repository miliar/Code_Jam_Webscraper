#include <iostream>
#include <fstream>
#include <vector>
#include <map>


using namespace std;

int main()
{
	int n;
	fstream fin("input.txt", fstream::in);
	fin >> n;

	for (int caseNo=1; caseNo <= n; ++caseNo) {
		vector<bool> mask(17, false);
		int r1;
		fin >> r1;

		int num;
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				fin >> num;
				if (i == r1)
				    mask[num] = true;	
			}
		}

		int r2;
		fin >> r2;

		vector<int> ans;
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				fin >> num;
				if (i == r2 && mask[num]) {
					ans.push_back(num);
				}
			}
		}

		cout << "Case #" << caseNo << ": ";
		if (ans.size() == 1) {
			cout << ans[0] << endl;
		} else if (ans.size() == 0) {
			cout << "Volunteer cheated!" <<endl;
		} else {
			cout << "Bad magician!" <<endl;
		}
	}

	return 0;
}
