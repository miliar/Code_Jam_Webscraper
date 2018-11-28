#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n, m;
		cin >> n >> m;
		vector<int> rows(n, 0);
		vector<int> cols(m, 0);
		vector<vector<int> > pattern(n, vector<int>(m));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				cin >> pattern[i][j];
				rows[i] = max(rows[i], pattern[i][j]);
				cols[j] = max(cols[j], pattern[i][j]);
			}
		
		bool ans = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (pattern[i][j] != min(rows[i], cols[j]))
					ans = false;
		
		cout << "Case #" << caseI << ": " << (ans ? "YES" : "NO") << endl;
	}
	
	return 0;
}
