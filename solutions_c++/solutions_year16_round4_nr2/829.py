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
#include <unordered_map>

using namespace std;

template <class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
    cout.precision(18);
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

double CalcTieProb(vector<double> p) {
    sort(p.begin(), p.end());
    vector<vector<double> > dp(p.size() + 1, vector<double>(p.size() + 1, 0.0));
    dp[0][0] = 1.0;
    for (int i = 0; i < p.size(); i++) {
        dp[i + 1][0] = (1 - p[i]) * dp[i][0];
        for (int j = 1; j <= i + 1; j++) {
            dp[i + 1][j] = p[i] * dp[i][j - 1] + (1 - p[i]) * dp[i][j];
        }
    }
    return dp[p.size()][p.size() / 2];
}

double SolveGreedy(vector<double> p, int k) {
    sort(p.begin(), p.end());
    vector<double> best;
    for (int i = 0; i < k / 2; i++) {
        best.push_back(p[i]);
        best.push_back(p[p.size() - i - 1]);
    }
    return CalcTieProb(best);
}


double SolveBruteForce(vector<double> p, int k) {
    int n = p.size();
    vector<double> cur;
    double maxProb = 0.0;
    cur.reserve(k);
    for (int i = 1; i < (1 << n); i++) {
        int bc = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                bc++;
            }
        }
        if (bc == k) {
            cur.clear();
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    cur.push_back(p[j]);
                }
            }
            maxProb = max(maxProb, CalcTieProb(cur));
        }
    }
    return maxProb;
}

double SolveTestCase() {
    int n, k;
    cin >> n >> k;
    vector<double> prob(n);
    for (int i = 0; i < n; i++) {
        cin >> prob[i];
    }
    double greedyProb = SolveGreedy(prob, k);
    double bfProb = SolveBruteForce(prob, k);
    if (fabs(greedyProb - bfProb) > 1e-6) {
        cerr << "Error!!!" << endl;
        cerr << n << " " << k << endl;
        cerr.precision(18);
        cerr << greedyProb << " " << bfProb << endl;
    }
    return bfProb;
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
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}