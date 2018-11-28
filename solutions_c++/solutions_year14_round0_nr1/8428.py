#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    freopen ("in", "r", stdin);
    freopen ("out", "w", stdout);
     
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
	int r1;
	cin >> r1;
	vector<vector<int> > vc1;
	for (int i = 0; i < 4; ++i) {
	    vector<int> v;
	    for (int j = 0; j < 4; ++j) {
		int x;
		cin >> x;
		v.push_back(x);
	    }
	    vc1.push_back(v);
	}
	int r2;
	cin >> r2;
	vector<vector<int> > vc2;
	for (int i = 0; i < 4; ++i) {
	    vector<int> v;
	    for (int j = 0; j < 4; ++j) {
		int x;
		cin >> x;
		v.push_back(x);
	    }
	    vc2.push_back(v);
	}
	sort (vc1[r1-1].begin(), vc1[r1-1].end());
	sort (vc2[r2-1].begin(), vc2[r2-1].end());
	int count = 0;
	int match = -1;
	for (int i = 0; i < 4; ++i) {
	    for (int j = 0; j < 4; ++j) {
		if (vc1[r1-1][i] == vc2[r2-1][j]) {
		    ++count;
		    match = vc1[r1-1][i];
		}
	    }
	}
	if (count == 1) {
	    cout << "Case #" << t << ": " << match << endl;
	}
	if (count > 1) {
	    cout << "Case #" << t << ": Bad magician!" << endl;
	}
	if (count == 0) {
	    cout << "Case #" << t << ": Volunteer cheated!" << endl;
	}
    }
}

