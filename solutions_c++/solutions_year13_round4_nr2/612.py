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
	cout << "Case #" << caseNumber << ": " << ans[0] << " " << ans[1] << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	long long p;
	cin >> n >> p;
	long long len = (1LL << n);
	long long pos = len  - p;

	vector<long long> ans(2, len - 1);
	if (pos == 0) {
		return ans;
	}
	long long q = 0;
	for (int i = n - 1; i > -1; i--) {
		if (pos & (1 << i)) {
			break;
		}
		q++;
	}
	ans[0] = 2 * (1LL << q) - 2;
	long long t = 0;
	bool hasZeroes = false;
	for (int i = n - 1; i > -1; i--) {
		if ((pos & (1 << i))) {
			t++;
			if (hasZeroes) break;
		} else {
			hasZeroes = true;
		}
	}
	ans[1] = len - (1 << t);
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<vector<long long>>() );

	return 0;
}