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
AnswerType SolveTestCase(const vector<long long>& fairNumbers) {
	long long a, b;
	cin >> a >> b;
	int ans = 0;
	for (int i = 0; i < fairNumbers.size(); i++) {
		if (fairNumbers[i] >= a && fairNumbers[i] <= b) ans++;
	}
	return ans;
}

bool IsPalyndrom(long long n) {
	vector<int> digits;
	while (n > 0) {
		digits.push_back(n % 10);
		n /= 10;
	}
	for (int i = 0; i < digits.size(); i++) {
		if (digits[i] != digits[digits.size() - i - 1]) {
			return false;
		}
	}
	return true;
}

void Compute(vector<long long>& fairNumbers) {
	fairNumbers.reserve(100000);
	for (long long n = 1; n <= 10000001; n++) {
		if (IsPalyndrom(n) && IsPalyndrom(n * n)) {
			fairNumbers.push_back(n * n);
		}
	}
}

int main()
{
	vector<long long> fairNumbers;
	Compute(fairNumbers);
	cerr << fairNumbers.size() << endl;
	for (int i = 0; i < fairNumbers.size(); i++) {
		cerr << fairNumbers[i] << endl;
	}
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(fairNumbers) );

	return 0;
}