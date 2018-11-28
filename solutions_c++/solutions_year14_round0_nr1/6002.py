#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getRow(int r) {

	vector<int> res;
	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j) {
			int x;
			cin >> x;
			if (i==r-1)
				res.push_back(x);
		}
	return res;
}

void solve(int cs) {
	
	int r1, r2;
	vector<int> v1, v2, ans;
	
	cin >> r1;
	v1 = getRow(r1);
	cin >> r2;
	v2 = getRow(r2);
	
	for (int i=0; i<4; ++i)
		if (find(v2.begin(), v2.end(), v1[i]) != v2.end())
			ans.push_back(v1[i]);
	
	cout << "Case #" << cs << ": ";
	if (ans.size()==1)
		cout << ans[0];
	else if (ans.size()>1)
		cout << "Bad magician!";
	else
		cout << "Volunteer cheated!";
	cout << endl;
}

int main() {
	
	int T;
	cin >> T;
	for (int t=1; t<=T; ++t) {		
		solve(t);
	}
	return 0;
}
