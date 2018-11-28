#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
	int a;
	cin >> a;
	a--;
	int c[4][4];
	for (int j = 0; j < 4; j++)
	    for (int k = 0; k < 4; k++)
		cin >> c[j][k];
	vector<int> candidate;
	for (int j = 0; j < 4; j++)
	    candidate.push_back(c[a][j]);

	cin >> a;
	a--;
	for (int j = 0; j < 4; j++)
	    for (int k = 0; k < 4; k++)
		cin >> c[j][k];
	vector<int> candidate2;
	for (int j = 0; j < 4; j++)
	    candidate2.push_back(c[a][j]);

	sort(candidate.begin(), candidate.end());
	sort(candidate2.begin(), candidate2.end());
	vector<int> v(4);
	auto it = set_intersection(candidate.begin(), candidate.end(), candidate2.begin(), candidate2.end(), v.begin());
	v.resize(it - v.begin());

	if (v.size() == 1)
	    cout << "Case #" << i << ": " << v[0] << endl;
	else if (v.size() > 1)
	    cout << "Case #" << i << ": " << "Bad magician!" << endl;
	else
	    cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
    }
}
