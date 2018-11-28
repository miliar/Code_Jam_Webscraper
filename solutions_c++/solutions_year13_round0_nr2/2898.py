#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

long long rec(int pos1, int pos2, long long left, int type, long long val)
{

}

int n,m;
vector<long long> a1, b1;
vector<int> a2,b2;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {		
		int n,m;
		cin >> n >> m;

		vector<vector<int> > field(n, vector<int>(m));
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				cin >> field[i][j];
			}
		}

		bool flag = true;
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				int val = field[i][j];
				bool row_flag = false;
				for (int k=0;k<n;k++) {
					if (field[k][j] > val) {
						row_flag = true;
						break;
					}
				}

				bool col_flag = false;
				for (int k=0;k<m;k++) {
					if (field[i][k] > val) {
						col_flag = true;
						break;
					}
				}

				if (row_flag && col_flag) {
					flag = false;
					break;
				}
			}
			if (!flag) break;
		}

		cout << "Case #" << (q+1) << ": ";
		cout << (flag ? "YES" : "NO") << endl; 
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}