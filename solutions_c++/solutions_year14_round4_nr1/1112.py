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
    int n, x;
    cin >> n >> x;
    vector<int> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i]; 
    }
    sort(s.begin(), s.end());
    int ans = n;
    for (int r = 0; 2 * r <= n; r++) {
        bool can = true;
        for (int i = 0; i < r; i++) {
            if (s[i] + s[2 * r - i - 1] > x) {
                can = false;
                break;
            }
        }
        if (can) {
            ans = min(ans, n - r);
        }
    }
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("A-small.in", "r", stdin);
	freopen("A-large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>() );

	return 0;
}