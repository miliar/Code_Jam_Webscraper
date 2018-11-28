#include <iostream>
#include <vector>
using namespace std;

int main() {
	int caseNum;

	cin >> caseNum;
	for (int i=1; i<=caseNum; i++) {
		vector<int> ans(2, 0);
		vector< vector< vector<int> > > arr(2, vector< vector<int> >(4, vector<int>(4, 0)));
		int output = 0;

		for (int j=0; j<ans.size(); j++) {
			cin >> ans[j];
			ans[j]--;
			for (int k=0; k<arr[j].size(); k++) {
				for (int m=0; m<arr[j][k].size(); m++)
					cin >> arr[j][k][m];
			}
		}
		for (int j=0; j<arr[0][ans[0]].size(); j++) {
			for (int k=0; k<arr[1][ans[1]].size(); k++) {
				if (arr[0][ans[0]][j] == arr[1][ans[1]][k]) {
					if (output == 0)
						output = arr[0][ans[0]][j];
					else
						output = -1;
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (output == -1)
			cout << "Bad magician!\n";
		else if (output == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << output << endl;
	}

	return 0;
}
