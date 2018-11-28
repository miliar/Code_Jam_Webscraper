#include <iostream>
#include <vector>
#include <algorithm>

#pragma warning(disable : 4996)

using namespace std;
int m[4][4];

void read_input(vector<int> & v)
{
	int t; cin >> t;
	for (int y = 0; y < 4; y++)
	for (int x = 0; x < 4; x++)
		cin >> m[x][y];
	for (int x = 0; x < 4; x++)
		v.push_back(m[x][t - 1]);
	sort(v.begin(), v.end());
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		vector<int> a, b, c(100);
		read_input(a);
		read_input(b);

		vector<int>::iterator it=set_intersection(a.begin(), a.end(), b.begin(), b.end(), c.begin());
		int size = it - c.begin();
		cout << "Case #" << i + 1 << ": ";
		if (size == 1)
			cout << c[0];
		else if (size == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}