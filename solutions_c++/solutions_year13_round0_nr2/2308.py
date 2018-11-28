#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n, m;
	cin >> n >> m;
	vector< vector<int> > lawn(n, vector<int>(m, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> lawn[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			bool f1 = true;
			for (int q = 0; q < m; q++) {
				if (lawn[i][q] > lawn[i][j]) {
					f1 = false;
				}
			}
			bool f2 = true;
			for (int q = 0; q < n; q++) {
				if (lawn[q][j] > lawn[i][j]) {
					f2 = false;
				}
			}
			if (!f1 && !f2) {
				return "NO";
			}
		}
	}
	return "YES";
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<string>() );

	return 0;
}