#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");

	int k;
	in >> k;

	for(int p = 1; p <= k; ++p) {
		int n, m;
		in >> n >> m;

		vector<vector<int>> a(n);
		vector<int> max_in_row(n, -1);
		vector<int> max_in_col(m, -1);

		for(int i = 0; i < n; ++i) {
			a[i].resize(m);
			for(int j = 0; j < m; ++j) {
				in >> a[i][j];
				max_in_row[i] = max(max_in_row[i], a[i][j]);
				max_in_col[j] = max(max_in_col[j], a[i][j]);
			}
		}

		bool yes = true;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				yes = yes && (a[i][j] == max_in_row[i] || a[i][j] == max_in_col[j]);
			}
		}

		out << "Case #" << p << ": " << (yes ? "YES" : "NO") << endl;
	}

	system("pause");
	return 0;
}

/*

*/
