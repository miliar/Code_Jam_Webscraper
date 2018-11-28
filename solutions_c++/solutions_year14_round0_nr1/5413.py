#include <iostream>
#include <vector>
using namespace std;

int a[5][5];
int b[5][5];
vector<int> v;

void work() {
	int n;
	cin >> n;
	n--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> a[i][j];
	int m;
	cin >> m;
	m--;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> b[i][j];

	v.clear();
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[n][i] == b[m][j])
				v.push_back(a[n][i]);

	if (v.size() == 0)
		cout << "Volunteer cheated!" << endl;
	else if (v.size() > 1)
		cout << "Bad magician!" << endl;
	else
		cout << v[0] << endl;

}

int main() {
	
	//freopen("G:/1.in", "r", stdin);
	//freopen("G:/1.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}